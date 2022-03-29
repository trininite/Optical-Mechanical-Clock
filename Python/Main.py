#Main
from datetime import datetime
from tkinter import *
import tkinter as ttk
import time
import serial
import random
#import threading

with open("LogFile", 'r+') as f:
    f.truncate(0)

print("RESET ARDUINO")
print("Starting Program in 3")
time.sleep(1)
print("Starting Program in 2")
time.sleep(1)
print("Starting Program in 1")
time.sleep(1)


ser = serial.Serial('/dev/ttyACM0', 9600)
global clk
clk = 0
global ss
ss = 0
global mm
mm = 0
global hh
hh = 0
global ticks
ticks = 0
global lasttick
lasttick = 9999

bigFont = font = ("Helvetica", 22)
normalFont = font = ("Helvetica", 16)

def noSerial_update_label():
    global ticks
    Ran = random.randint(1000,10000)
    ohmCounter.config(text = Ran)
    tickCounter.config(text = Ran)
    timeCounter.config(text = Ran)

    root.after(500, noSerial_update_label)


def update_label():
    global clk
    global ss
    global mm
    global hh
    global lasttick
    if ser.in_waiting:
        clk += 1 #add 1 to operation counter

        RX = ser.readline().decode('utf-8', errors = 'ignore')  #make RX equal to incoming aruino data 

        RXLen = len(RX) #Make RXLen equal to the length of RX

        RXC = RX.index(":") #make RXC equal to position of dividing colon

        R = RX[:RXC] #make R equal to value(s) before dividing colon (Resistance)

        ticks = RX[RXC+1:RXLen] #make ticks equal to value(s) after colon (Ticks)

        if int(ticks)!= 0: #If tick count isn't 0 (prevent seconds value from going up on the first operation)
            if int(ticks) % 2 == 0: #If the parameters of the clock constitute a tick
                if lasttick != ticks: #If the tick is not a duplicate
                    ss += 1 #Add 1 second
                    lasttick = ticks #Set current tick val to lasttick val; used to prevent duplicate ticks on line 63

        timeFormatted = str(hh), str(mm),  str(ss) #Format the time 

        nowRaw = datetime.now()

        now = nowRaw.strftime("%H:%M:%S")
        
        logData = "System Time:" + str(now) + "Resistance Value:" + str(R) + "Tick Count:" + str(ticks) + "" 

        log = open('LogFile','a') #Open log file
        log.writelines(str(RX) + str(R) + str(clk) + str(timeFormatted)) #Write values
        log.close #Close log file
        
        ohmCounter.config(text = R) #Update label with resistance
        tickCounter.config(text = ticks) #Update tick count
        timeCounter.config(text = timeFormatted) #Update time count

        root.after(100, update_label)#Calls update_label function again after 1 second.
    else:
        root.after(100, update_label)#Calls update_label function again after 1 second.


root = ttk.Tk()
root.geometry('500x400')

#At some point all the widgets need to be organized into frames 
#Then each fram should be put in a seperate file linked with json
#dataFrame = ttk.Frame(
#    root
#)

#Static Labels

#Lables resistance output
ohmLabel = ttk.Label(
    root,
    text = "Resistance:",
    font = (bigFont)
)
#Lables tick counter
tickLabel = ttk.Label( 
    root,
    text = "Ticks:",
    font = (bigFont)
)

#Lables time counter
timeLabel = ttk.Label( 
    root,
    text = "Time:",
    font = (bigFont)
)

#Output Labels
ohmCounter = ttk.Label(
    root,
    text = "000000000",
    font = (normalFont),
    relief = SOLID 
)

#Outputs incoming tick count
tickCounter = ttk.Label( 
    root,
    text = "000000000",
    font = normalFont
)

#Outputs calculated time
timeCounter = ttk.Label( 
    root,
    text = "000000000",
    font = normalFont
)

#Functions

quitButton = ttk.Button(
    root,
    text = "Quit",
    command = quit
)

motorToggle = ttk.Button(
    root,
    text = "Off",
    command = print
)

#Grid

#Static Labels
ohmLabel.grid(
    column = 0,
    row = 0
)

tickLabel.grid(
    column = 0,
    row = 2
)

timeLabel.grid(
    column = 0,
    row = 4
)

#Output Labels
ohmCounter.grid(
    column = 0,
    row = 1
)

tickCounter.grid(
    column = 0,
    row = 3
)

timeCounter.grid(
    column = 0,
    row = 5
)

#Functions

motorToggle.grid(
    column = 0,
    row = 6
)



quitButton.grid(
    column = 0,
    row = 7,
    sticky = S
)

update_label()

root.grid
root.mainloop()




