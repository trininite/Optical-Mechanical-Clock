#Calibrate ticks per second

import serial, time

global ser
ser = serial.Serial("/dev/ttyUSB0", 115200)

global dupeLatch 
dupeLatch = False

global RThresh
RThresh = 5

global ticks
ticks = 0

t_end = time.time() + 60

while time.time() < t_end:
    R = int(ser.readline().decode('utf-8', errors = "ignore"))
    
    if R <= RThresh:

        if dupeLatch == False:
            ticks += 1
            dupeLatch = True

        elif dupeLatch == True:
            pass


    elif R > RThresh + 10:
        dupeLatch = False

TPS = ticks / 60

print(f"Ticks per second: {TPS}")


