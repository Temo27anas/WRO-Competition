import keyboard, serial
from numpy import var
import time


#ask seria port
serial_port = input("Enter serial port: COM")
port = "COM" + serial_port
var = serial.Serial(port, 9600)

print("start")

while True:
    keyboardList= [0,0,0,0]

    if keyboard.is_pressed('w'):
        var.write(b'w')
        print("w")

    elif keyboard.is_pressed('s'):
        var.write(b's')
        print("s")
        
    elif keyboard.is_pressed('a'):
        var.write(b'a')
        print("a")
        
        
    elif keyboard.is_pressed('d'):
        var.write(b'd')
        print("d")
        
     # send the data to the arduino
    time.sleep(0.1)
   
    
