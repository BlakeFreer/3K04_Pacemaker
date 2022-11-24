import serial 

with serial.Serial('COM6', 115200) as ser:
    val1= 6
    val2 = 4 
    val3 = 700

    #arr  = [12,3,34,5,67,567,2,2,34]

    first = val1.to_bytes(1,"big") 
    second = val2.to_bytes(1,"big")
    third = val3.to_bytes(2,"big")
    
  
    print(first+second+third)
    ser.write(first+second+third)
    ##ser.write(b'sdsdsfd')
    x = ser.read(4)
    
    print(x)

