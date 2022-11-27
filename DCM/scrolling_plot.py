"""
This is a Python script for plotting in real time data of the MPU9250 which are collected on a com port
@author : Mohamed SANA
@contact : Follow me on github.com/Sanahm/
@licence : Under GNU licence
@date : 30/04/2017
"""

import serial
import time
import numpy as np
from matplotlib import pyplot as plt
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import os
import pyqtgraph.console
import PyQt5
import csv
import pandas as pd
from analyzer import *

pg.setConfigOption('background','w')
pg.setConfigOption('foreground', 'k')
##initialization of Qt
app = QtGui.QApplication([])
## Define a top-level widget to hold everything
w = QtGui.QWidget()
w.setWindowTitle("Painter's Grip Pro")
wb = QtGui.QWidget(w)
win = pg.GraphicsWindow()

#screens are numerated like this: lr11 means first line and first column
# Create the 3 colour bands on the Tremor Gauge
lrg = pg.LinearRegionItem(values=[0, 70],orientation="horizontal",brush=pg.mkBrush(color=(0,255,0,100)))
lry = pg.LinearRegionItem(values=[70, 110],orientation="horizontal",brush=pg.mkBrush(color=(255,255,0,100)))
lrr = pg.LinearRegionItem(values=[110, 200],orientation="horizontal",brush=pg.mkBrush(color=(255,0,0,100)))

#the idea of scrolling plot is to define a matrix of data with fix length and to
#update it each time you receive data

#here the length is set to 300. 3 means the 3-dimension. 
data1 = np.zeros((3,300)); #contains acc_x, acc_y and acc_z 
data2 = np.zeros((3,300)); #contains gyr_x, gyr_y and gyr_z
data3 = np.zeros((3,300)); #contains mag_x, mag_y and mag_z

p11 = win.addPlot()
p11.addLegend(offset=(10,10))
p11.setYRange(0,150,padding=0)
p11.addItem(lrg,name='region11g')
p11.addItem(lry,name='region11y')
p11.addItem(lrr,name='region11r')

p12 = win.addPlot()
p12.addLegend(offset=(10,10))

p21 = win.addPlot()
p21.addLegend(offset=(10,10))
p22 = win.addPlot()
p22.addLegend(offset=(10,10))

win.nextRow()

curve11 = p11.plot(data1[0],pen = pg.mkPen(color=(100,100,100),width=3),name = 'Tremor Gauge')
curve12 = p12.plot(data2[0],pen = (0,3),name = 'Accel X')
curve13 = p21.plot(data1[1],pen = (1,3),name = 'Accel Y')
curve14 = p22.plot(data2[1],pen = (2,3),name = 'Accel Z')

# My variables

# Serial Connection
com = 'COM7'
speed = 38400

col_names = ['ax', 'ay', 'az', 'gx', 'gy', 'gz','mx', 'my', 'mz', 't']

ard_start = None
master_list = []
new_data_size = 20
window_size = 200
led_status = 1
gauge_value = 0

import traceback

try:
    # Initialize Serial connecton
    serie = serial.Serial(port=com,baudrate=speed, timeout=10)
    print("CONNECTED TO "+com)
    serie.flush()
    serie.write("1".encode("utf-8"))    # Reset LED to Green
    start = time.time()
except:
    # Error in creatng a Serial connection
    print("An error occured: unable to open the specified port " +com)
    exit(0)

tps = np.zeros(300) #you need time to, the same length as data
if(not(serie.readable())):
    print("unable to read available value on port\n"+com)

def update():
    global data1,data2,data3, curve11,curve12,curve13,curve14,ard_start,master_list,col_names,led_status,gauge_value
    line = str(serie.readline(),'utf-8')
    
    acc = []
    gyr = []
    mag = []
    line2 = line
    line = line.split(" ")

    #for each line I collect data like this "acc_x acc_y acc_z gyr_x ... mag_z"
    try:
        tab = [float(i) for i in line]
    except ValueError:
        print("Error with line:",line2)
        return
    if len(tab) != 10:
        return

    acc = tab[0:3]  # read the 3 values of acc
    gyr = tab[3:6]  # read the 3 values of gyr
    mag = tab[6:9]  # read the 3 values of mag
    t = tab[9]      # read time data
    if not ard_start:
        ard_start = tab[9]
    t -= ard_start
    tab[9] = t

    # Save each data row to temporary list
    master_list.append(tab)

    if len(master_list) >= new_data_size + window_size:
        #Call Sam's analysis - return led status
        
        # Create analyzer object
        anl = Analyzer(master_list, col_names)
        # Analyze data
        anl.analyze_spikes(roll_sum_win_size = window_size)
        
        # Get led status and tremot gauge value and write to serial
        led_status, gauge_value = anl.get_LED(window_size)
        serie.write(str(led_status).encode("utf-8"))

        # Truncate data
        master_list = master_list[-window_size:]

    tps[:-1] = tps[1:]
    tps[-1] = time.time()-start
    
    data1[:,:-1] = data1[:,1:]  # shift data in the array one sample left
    data2[:,:-1] = data2[:,1:]
    data3[:,:-1] = data3[:,1:]
    
    data1[:,-1] = acc
    data2[:,-1] = gauge_value
    data3[:,-1] = mag

    # Display data on the 4 charts
    curve11.setData(data2[0])   # Tremor Gauge
    curve12.setData(data1[0])   # Acc.x
    curve13.setData(data1[1])   # Acc.y
    curve14.setData(data1[2])   # Acc.z


timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(6)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
    
serie.close()
