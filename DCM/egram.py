from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import serial as sr
import time

root = tk.Tk()
root.title("Electrogram")
root.configure(background = 'black')
root.geometry("700x500")



#Data inputs
data = np.array([])
cond = False

def plot_data():
	global cond
	global data

	if (cond == True):
		a = s.readline()

		#Check if data is fits in plot
		if (len(data) < 100):
			data = np.append(data, float(a[0:4]))
		else:
			data[0:99] = data[1:100]
			data[99] = float(a[0:4]) 

		lines.set_xdata(np.arrange(0, len(data)))
		lines.set_ydata(data)

		canvas.draw()
	root.after(1,plot_data)

def plot_start():
	global cond 
	cond = True
	s.reset_input_buffer()

def plot_stop():
	global cond
	cond = False

#plot object
fig = Figure()
axis = fig.add_subplot(111)

axis.set_title('Serial Data')
axis.set_xlabel('Time')
axis.set_ylabel('Voltage')
axis.set_xlim(0,100)
axis.set_ylim(-0.5,6)

#Updates plot as it is receiving serial data
lines = axis.plot([],[])[0]

canvas = FigureCanvasTkAgg(fig, master = root)
canvas.get_tk_widget().place(x = 10, y=10, width = 500, height = 400)
canvas.draw()



#buttons (Atrial/Ventrical)
root.update()
start = tk.Button(root, text = "Plot", font = ('calibri', 12), command = lambda: plot_start())
start.place(x = 100, y = 450)

root.update()
stop = tk.Button(root, text = "Stop", font = ('calibri', 12), command = lambda: plot_stop())
stop.place(x = start.winfo_x() + start.winfo_reqwidth() + 20, y = 450)


#serial communication (UART)
s = sr.serial('COM3', 115200)
s.reset_input_buffer()





root.after(1, plot_data)
root.mainloop()