import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#serial libraries
import struct
from serial import Serial

ser = Serial()
ser.port = 'COM3'
ser.baudrate = 115200
ser.timeout = 0.5
ser.dtr = 0
ser.open()
print("Is Serial Port Open:", ser.isOpen())


fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
x, y1, y2= [], [], []



while True:

    #Read echo Parameters
    ser.readline()
    num1 = num1.decode('utf')#int[0]
    num2 = num2.decode('utf')#int[1]
    
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