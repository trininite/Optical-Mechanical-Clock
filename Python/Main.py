#Main
from tkinter import *
import tkinter as ttk
import time
import serial
import threading

global Vin
global VOut
global RRef
global RTest

Vin = 5
VOut = 0
RRef = 1000
RTest = 1300000 


global ticks
bigFont = font = ("Helvetica", 22)
ser = serial.Serial('/dev/ttyACM0', 9600)
ticks = 0

def update_label():
    A0 = int(ser.readline())
    Vout = (Vin * A0) / 1023
    R = RRef * (1 / ((Vin / Vout) -1))  

    ohmCounter.config(text=str(A0)) #Update label with next text.

    root.after(1000, update_label)#calls update_label function again after 1 second.

root = ttk.Tk()
root.geometry('500x400')
root.geometry

#Static Labels
ohmLabel = ttk.Label(
    root,
    text = "Resistance:",
    font = (bigFont)
)

tickLabel = ttk.Label( #Lables tick counter
    root,
    text = "Ticks:",
    font = (bigFont)
)

timeLabel = ttk.Label( #Lables time counter
    root,
    text = "Time:",
    font = (bigFont)
)

#Output Labels
ohmCounter = ttk.Label(
    root,
    text = "" 
)

tickCounter = ttk.Label( #Outputs incoming tick count
    root,
    text = ""
)

timeCounter = ttk.Label( #Outputs calculated time
    root,
    text = "",
    font = (22)
)

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

#--------------------

ohmCounter.grid(
    column = 0,
    row = 1
)

tickCounter.grid(
    column = 0,
    row = 3
)

timeLabel.grid(
    column = 0,
    row = 5
)


update_label()

root.grid
root.mainloop()
