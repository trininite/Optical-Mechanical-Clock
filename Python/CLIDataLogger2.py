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

#Create tick counter
global ticks
ticks = 0

#Create resistance threshold
global RThresh
RThresh = 10

#Create duplicate detection latch
global dupeLatch
dupeLatch = False

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
def genPacket(R, Ticks, first):
    if first == True:
        iH = h
        iM = m
        iS = s
        packet = "INITIAL TICK TIME: " + h + m + s + ""
    
    if first == False:
        return

def calcError(mode, h, m, s):
    if mode == "edit":
        iH = h
        iM = m
        iS = s
    elif mode == "calc"

#Get serial data
def evalRx(R):
    global ticks, RThresh, dupeLatch, ticksPerSec
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
            
            calcError("edit", iH, iM, iS)

            genPacket(R, ticks, True, iH, iM, iS, 0, 0, 0)

        #If unique
        if dupeLatch == False:
            ticks += 1
            dupeLatch = True
            
            if ticks % ticksPerSec == 0:
                cS += 1
                a1s = True
            if cS % 60 == 0:
                cS = 0
                cM += 1
            if cM % 60 == 0:
                cM = 0
                cH += 1
            
            genPacket(R, ticks, )


                
            
            
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

