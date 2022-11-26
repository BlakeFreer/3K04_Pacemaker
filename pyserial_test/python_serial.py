import serial
import serial.tools.list_ports
import struct
import time 


start = b'\x21'
arr= []
val = 0 
for i in range(0,35): 
    arr.append(1)
    """
    if ((i == 4) or(i==8) or (i ==9) or (i ==13) or (i ==25) or (i ==30)):
        val = val + i*10
    elif ((i == 24) or ( i ==29)):
        val = val + i *4
    elif ((i ==21) or (i ==26 )): 
        val = val + i / 10 
    elif ((i == 23) or (i ==28)):
        val = val +i/100
    else: 
        val = val + i

    """

print("val " ,val)

arr[0] = 10
sig =struct.pack("B", 100)

for i in arr:
    sig = sig+ struct.pack("B",i)
sig = sig + start
print("sig ", sig , "len ", len(sig) )

with serial.Serial('COM6', 115200) as ser:
    print(sig)
    ser.write(sig)


"""

red_en = struct.pack("B",0)
#random = struct.pack("f", 0.44323)

sig = start +red_en +red_en #+ random 
print(len(sig))
"""
