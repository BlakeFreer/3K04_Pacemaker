import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial
import time
import tkinter as tk

#initialize serial port
ser = serial.Serial()
ser.port = 'COM3' #Arduino serial port
ser.baudrate = 115200
ser.timeout = 0.5
ser.dtr = 0
ser.open()

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
x, y1, y2 = [], [], []


while True:
    line=ser.readline()

    num1 = int(line[0]) 
    num2 = int(line[1])

    x.append(i)
    y1.append(num1)
    y2.append(num2)

    ax.plot(x, y1, color='b')
    ax.plot(x, y2, color='r')
    
    fig.canvas.draw()

    ax.set_xlim(left=max(0, i-50), right=i+50)
    
    time.sleep(0.1)
    i += 1

plt.ion()
plt.draw()
ser.close()