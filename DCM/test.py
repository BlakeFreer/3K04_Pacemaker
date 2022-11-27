import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pyautogui as gui
import tkinter as tk
import numpy as np
import serial as sr
matplotlib.use('TkAgg')

# ------------Global Variables ------------#
data_x = np.array([])
data_y = np.array([])

screen_width, screen_height = gui.size()
cond = False


def mapValues(num, x_or_y):
    global screen_width, screen_height
    maxValX = 1023
    maxValY = 1023
    if x_or_y == 1:
        proportion = num / maxValX
        new_val = round(screen_width * proportion)
        if new_val > screen_width:
            new_val = screen_width
    else:
        proportion = num / maxValY
        new_val = round(screen_height * proportion)
        if new_val > screen_height:
            new_val = screen_height
    if new_val < 0:
        new_val = 0
    return new_val


def plot_data():
    global cond, data_x, data_y, s
    len_line = 4
    if cond:  # to prevent continuous data logging
        data = s.readline()  # read and decode the serial data
        data = data.decode('utf')
        try:
            coordinates = data.split()  # split the incoming str data into the x and y components
            x_val = coordinates[0]
            y_val = coordinates[1]
            # print(x_val, y_val, type(x_val))
            x_val = mapValues(int(x_val), 1)  # map the values to an arbitrary range
            y_val = mapValues(int(y_val), 2)
            print(x_val, y_val)
            # print('length of array: ', len(data_x))
            # print(data_x, '\n', data_y)
            if len(data_x) < len_line:  # keep the length of the x,y data consistently at whatever value we want
                data_x = np.append(data_x, x_val)
                data_y = np.append(data_y, 320 - y_val)
            else:  # shift all the values back in the list and add the new one to the end
                data_x[0:len_line-1] = data_x[1:len_line]
                data_x[len_line-1] = x_val
                data_y[0:len_line-1] = data_y[1:len_line]
                data_y[len_line-1] = y_val

            # update the x and y data of the line
            line1.set_xdata(data_x)
            line1.set_ydata(data_y)
            print('Line data: ', line1.get_xydata())

            # update the canvas
            canvas.draw()
            canvas.flush_events()
        except Exception as e:
            print(e)
    root.after(1, plot_data)


def start_plot():
    global s, cond
    s.reset_input_buffer()
    cond = True


def stop_plot():
    global cond, s
    cond = False


if __name__ == '__main__':
    print('Starting...')

    # ----------main GUI code --------------------#
    root = tk.Tk()
    root.title('Real Time Motus Hand')
    root.configure(background='black')
    app_width = 1200
    app_height = 800
    x_offset = (screen_width - app_width) / 2
    y_offset = (screen_height - app_height) / 2
    root.geometry(f'{app_width}x{app_height}+{int(x_offset)}+{int(y_offset)}')

    # ---------- create plot object on figure ----------#
    fig = Figure()
    # customize parameters
    ax = fig.add_subplot(111)
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_xlim(0, screen_width)
    ax.set_ylim(0, screen_height)
    #  create line object to control data
    line1 = ax.plot([], [])[0]
    #  define figure height and width and placement
    plot_width = 800
    plot_height = 600
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=(app_width - plot_width) / 2, y=(app_height - plot_height) / 2,
                                 width=plot_width, height=plot_height)
    canvas.draw()

    # ----------create start and stop buttons -------------
    start = tk.Button(root, text='start drawing', font=('calbiri', 12), command=lambda: start_plot())
    start.place(x=100, y=app_height - 50)

    stop = tk.Button(root, text='stop drawing', font=('calbiri', 12), command=lambda: stop_plot())
    stop.place(x=300, y=app_height - 50)

    # --------start serial communication ---------
    s = sr.Serial('COM3', 115200)
    s.reset_input_buffer()

    root.after(1, plot_data)
    root.mainloop()