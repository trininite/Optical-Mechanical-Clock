#Main
from tkinter import *
import tkinter as ttk
import time
import serial
import threading


print("RESET ARDUINO")
time.sleep(5)


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



def update_label():
    global clk
    global ss
    global mm
    global hh
    global lasttick
    if ser.in_waiting:
        clk += 1 #add 1 to operation counter
        RX = ser.readline() #make RX equal to incoming aruino data 
        RXD = RX.decode('utf-8', errors = 'ignore') #decode to utf-8
        RXLen = len(RXD) #determine length of RX
        RXC = RXD.index(":") #make RXC equal to position of dividing colon
        R = RXD[:RXC] #make R equal to value before dividing colon
        ticks = RXD[RXC+1:RXLen] #make ticks equal to value after colon

        if int(ticks)!= 0:
            if int(ticks) % 2 == 0:
                if lasttick != ticks:
                    ss += 1
                    lasttick = ticks

        timet = str(hh), str(mm),  str(ss) 

        log = open('LogFile','a') #Open log file
        log.writelines(str(RXD) + str(R) + str(clk) + str(timet)) #Write values
        log.close #Close log file
        ohmCounter.config(text = R) #Update label with resistance
        tickCounter.config(text = ticks) #Update tick count
        timeCounter.config(text = timet) #Update time count
        root.after(1000, update_label)#Calls update_label function again after 1 second.
    else:
        root.after(50, update_label)#Calls update_label function again after 1 second.


root = ttk.Tk()
root.geometry('500x400')
root.geometry

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
    text = "",
    font = normalFont
)

#Functions

quitButton = ttk.Button(
    root,
    text = "Quit",
    command = quit
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
quitButton.grid(
    column = 0,
    row = 6,
    sticky = S
)

update_label()

root.grid
root.mainloop()




