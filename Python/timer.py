#Timer

import serial
import sys
from datetime import *
import time

#Increase recursion limit
sys.setrecursionlimit(10**6)

global tps
tps = 7.833334

global RThresh
RThresh = 3

global ser
ser = serial.Serial("/dev/ttyUSB0", 115200)

global ticks
ticks = 0

global dupeLatch 
dupeLatch = False

print("Enter timer length in seconds:")
timerLen = input()

global endTick
endTick1 = float(timerLen) * tps 
endTick = int(endTick1)


print(endTick)
time.sleep(1)

def main():
    global endTick, ticks, dupeLatch
    
    while ticks < endTick:
        RRaw = ser.readline().decode('utf-8', errors = "ignore")
        R = int(RRaw)

        if R <= RThresh:
            #If first tick
            if ticks <= 0:
                start = datetime.now()
                planEnd = start + timedelta(seconds = int(timerLen))    

            #If unique
            if dupeLatch == False:
                ticks += 1
                dupeLatch = True

        elif R > 10:
            dupeLatch = False

        if ticks >= endTick:
            end = datetime.now()
            
            if planEnd > end:
                diff = planEnd - end

            elif planEnd < end:
                diff = end - planEnd

            else:
                diff = 0
            
            startform = start.strftime("%H:%M:%S")
            planEndform = planEnd.strftime("%H:%M:%S")
            endform = end.strftime("%H:%M:%S")

            print()
            print(f"Start time: {startform} | Projected End Time: {planEndform} | Real End: {endform} | Error: {diff}")
            quit()

            
        print(R, ticks)

main()
        


    
