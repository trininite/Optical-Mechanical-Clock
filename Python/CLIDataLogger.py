#CLI Serial Data Logger
from datetime import datetime
import time
import serial

global LogPath #Path to log file
LogPath = "/home/trident/Documents/Optical-Mechanical-Clock/CLILogFile"

global ser #Path to arduino serial device file
ser = serial.Serial('/dev/ttyUSB0', 9600)

global clk #Operation counter
clk = 0

global ss #Seconds counter
ss = 0

global mm #Minute counter
mm = 0

global hh #Hour counter
hh = 0 

global ticks #Tick counter
ticks = 0

global lastR
lastR = 0

global tickThresh
tickThresh = 9999

global OnFirstTick
OnFirstTick = False

with open (LogPath, 'r+') as f:
    f.truncate(0)

#Functions

def logPacket():

def genPacket(R, T, S, M, H):
    packet = f("Resistance:{R} | Ticks:{T} | Seconds:{S} | Minutes:{M} | Hours:{H} |  ")
    

def evalData(R, RealTime):
    global ss
    global mm
    global hh
    global lastR
    global ticks
    global tickThresh
    
    if R != lastR
        if R >= tickThresh:
            ticks += 1
    
    lastR = R

    #"ticks per second" WILL CAUSE ERRORS - REPLACE ASAP"
    if ticks % "ticks per second" == 0:
        ss += 1
    
    if ss % 60 == 0:
        ss = 0
        mm += 1

    if mm % 60 == 0:
        mm = 0
        hh += 1


    genPacket()



def pullData():
    global clk
    global OnFirstTick
    global tickThresh
    
    R = ser.readline().decode('utf-8', error = 'ignore')
    
    if OnFirstTick == False:
        if R >= tickThresh
            startNow  = datetime.now()
            startH = startNow.strftime("%H")
            startM = startNow.strftime("%M")
            startS = startNow.strftime("%S")
                
            initData = f("START HERE | Real Time:{startH}:{startM}:{startS} | Resistance:{R} | Operation Count:{clk}" )

            log = open(LogPath, 'a')
            log.writelines(initData)
            log.close
            
            clk += 1
            noMas = True
            pullData
    
    #If data is available
    if ser.in_waiting == True: 
        RX = ser.readline().decode('utf-8', error = 'ignore')
        RealNow = datetime.now()
        RealH = RealNow.strftime("%H")
        RealM = RealNow.strftime("%M")
        RealS = RealNow.strftime("%S")
        
        #Not really needed
        #RXLen = len(RX) #Find length of RX and set RXLen equal to it
        
        RXC = RX.index(":") #Find position of indexing colon and set RXC to it
        
        R = RX[:RXC] #Split resistance from RX and set R equal to it
        
        #Might only send resistance from arduino then do all interperatation python side
        #Ts = RX[RXC+1:] #Split ticks from RX and set Ts equal to it
        
        evalData(R, RealTime) #Call data evaluator function
        
def pullRand
    

