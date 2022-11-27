import tkinter as tk
import serial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import time

#Tkinter------------------------------------
root = tk.Tk()
root.title("Electrogram")
root.configure(background = 'black')
root.geometry("700x500")

i = 0
x, y1, y2 = [], [], []
cond = False

#Start button
def plot_start():
    global cond 
    cond = True
    ser.reset_input_buffer()

#Stop button
def plot_stop():
    global cond
    cond = False
    ser.reset_input_buffer()
def plot_data():
    global cond
    i = 0
    lines = axis.plot([],[])[0]

    while (cond == True):
        line = ser.readline()
        num1 = int(line[0]) 
        num2 = int(line[1])
        x.append(i)
        y1.append(num1)
        y2.append(num2)

        axis.plot(x, y1, color='b')
        axis.plot(x, y2, color='r')
    
        fig.canvas.draw()

        axis.set_xlim(left=max(0, i-50), right=i+50)
        lines.set_xdata(x)
        lines.set_ydata(y1)
        lines.set_ydata(y2)
        fig.canvas.draw()

        time.sleep(0.1)
        i += 1
    axis.plot(x, y1, color='b')
    axis.plot(x, y2, color='r')
    fig.canvas.draw()
    root.after(1, plot_data)
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.get_tk_widget().place(x = 10, y=10, width = 500, height = 400)
    fig.canvas.draw()

#plot
fig = Figure()
axis = fig.add_subplot(111)

axis.set_title('Serial Data')
axis.set_xlabel('Time')
axis.set_ylabel('Voltage')
axis.set_xlim(0,100)
axis.set_ylim(-0.5,6)

#Update plot as it is receiving serial data
#lines = axis.plot([],[])[0]

#canvas = FigureCanvasTkAgg(fig, master = root)
#canvas.get_tk_widget().place(x = 10, y=10, width = 500, height = 400)
#canvas.draw()

#Buttons
root.update()
start = tk.Button(root, text = "Plot", font = ('calibri', 12), command = lambda: plot_start())
start.place(x = 100, y = 450)

root.update()
stop = tk.Button(root, text = "Stop", font = ('calibri', 12), command = lambda: plot_stop())
stop.place(x = start.winfo_x() + start.winfo_reqwidth() + 20, y = 450)

#---------------------------------------------

#initialize serial port
ser = serial.Serial()
ser.port = 'COM3' #Arduino serial port
ser.baudrate = 115200
ser.timeout = 0.5
ser.dtr = 0
ser.open()


root.after(1, plot_data)
root.mainloop()