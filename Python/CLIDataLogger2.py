#CLIDataLogger3

import serial
import sys
from datetime import datetime

#Increase recursion limit
sys.setrecursionlimit(10**6)

#Initialize serial connection
global ser
ser = serial.Serial("/dev/ttyACM0", 115200)

#Create log file path object
global LogPath
LogPath = "/home/trident/Documents/Optical-Mechanical-Clock/CLILogFile"
#Clear log file
with open(LogPath, "r+") as log:
    log.truncate(0)
    log.close

#Create operation counter
global clk
clk = 0

#Create tick counter
global ticks
ticks = 0

#Create resistance threshold
global RThresh
RThresh = 10

#Create duplicate detection latch
global dupeLatch
dupeLatch = False

#First tick time variables
global fs
fs = 0
global fm
fm = 0
global fh
fh = 0 

#Log packet
def logRx(packet):
    global clk
    log = open(LogPath, 'a')
    log.writelines(packet)
    log.close
    clk += 1
    return

#Generate packet
def genPacket(R, Ticks, first):
    if first == True:
        packet = str(clk) + "Resistance:" + str(R) + "Ticks:" + str(Ticks)
        

#Get serial data
def evalRx(R):
    global ticks, RThresh, dupeLatch
    realTime = datetime.now()
    realH = 
    realM = 
    realS =

    #If a tick
    if R <= RThresh:

        #If not a duplicate
        if dupeLatch == False:
        
            #If first tick
            if ticks == 0:
                dupeLatch = True
                ticks += 1
                genPacket(R, ticks, True)
            
            #If not first tick
            elif ticks != 0:
                dupeLatch = False
                ticks += 1
                genPacket(R, ticks, False)

        #If a duplicate
        elif dupeLatch == True:
            genPacket(R, ticks, False)

    #If not a tick
    elif R > RThresh:
        dupeLatch == False
        genPacket(R, ticks, False)

    #If anything else, quit
    else:
        print("ERROR")
        quit()

def pullRx():
    global ser
    
    R = ser.readline().decode('utf-8', errors = "ignore")

    evalRx(R)



#Start loop
getRx()

