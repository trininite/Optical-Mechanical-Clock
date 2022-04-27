#CLIDataLogger3

import serial
import sys
from datetime import datetime

#-----------------------------------------------------------------------------------------------

#Increase recursion limit
sys.setrecursionlimit(10**6)

#-----------------------------------------------------------------------------------------------

#Tuning
#Create resistance threshold
global RThresh
RThresh = 10

#Normal amount of ticks per second
global ticksPerSec
ticksPerSec = 60

#-----------------------------------------------------------------------------------------------

#Data transfer/logging
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

#-----------------------------------------------------------------------------------------------

#Flags
#Create operation counter
global clk
clk = 0

#Create global operatio counter
global globclk
globclk = 0

#Create tick counter
global ticks
ticks = 0

#Create resistance threshold
global RThresh
RThresh = 10

#Create duplicate detection latch
global dupeLatch
dupeLatch = False

#Initial tick time
global iH, iM, iS
iH = 0
iM = 0
iS = 0

#-----------------------------------------------------------------------------------------------

#Functions <more text>
#Log packet
def logRx(packet):
    global clk
    log = open(LogPath, 'a')
    log.writelines(packet)
    log.close
    return

#Generate packet
def genPacket(R, Ticks, first, h, m, s):
    if first == True:
        packet = "INITIAL TICK TIME: " + h + m + s + ""
        

#Get serial data
def evalRx(R):
    global ticks, RThresh, dupeLatch, iH, iM, iS
    nowRaw = datetime.now()
    nH = nowRaw.strftime("%H")
    nM = nowRaw.strftime("%M")
    nS = nowRaw.strftime("%S")

    #If a tick
    if R <= RThresh:
         
        #If first tick
        if ticks <= 0:
            iH = nH
            iM = nM
            iS = nS
            genPacket(R, ticks, )

        #If unique
        if dupeLatch == False:
            ticks += 1
            dupeLatch = True
            
            
        #If not unique
        elif dupeLatch == True:
            calcTime(R, ticks, nH, nM, nS)

    #If not a tick
    elif R > RThresh:
        dupeLatch == False
        calcTime(R, ticks, nH, nM, nS)
        
    #If anything else, quit
    else:
        print("ERROR")
        quit()

    

def pullRx():
    global ser
    
    R = ser.readline().decode('utf-8', errors = "ignore")
    evalRx(R)


#Start loop

pullRx()

