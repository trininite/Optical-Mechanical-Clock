#Serial-Test-CLI

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

calctimesec = 0
calctimemin = 0

while True:
    data = ser.readline().decode("utf-8")
    if data % 600 == 0:
        calctimesec += 1
    if calctimesec % 60 == 0:
        calctimemin
    print(data)
    time.sleep(1)
