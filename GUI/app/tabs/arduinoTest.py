#THIS IS A TEMPORARY FILE
#IF YOU SEE THIS IN A FINAL BUILD, DELETE IT

import serial
# import serial.tools.list_ports
import time

arduino = serial.Serial(port='/dev/tty.usbmodem834301', baudrate=115200, timeout=.1)
x = 0
y = 0
# for p in list(serial.tools.list_ports.comports()):
#     print(p)
while True:
    data = arduino.readline().decode('utf-8')
    data = data.strip()
    if(len(data) > 0):
        x = int(data[:4])
        y = int(data[5:9])
    print(x)
    print(y)
    time.sleep(0.01)