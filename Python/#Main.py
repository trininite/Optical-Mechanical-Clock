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
    A0 = float(ser.readline())
    Vout = (Vin * A0) / 1023
    R = RRef * (1 / ((Vin / Vout) -1))  

    ohmLabel.config(text=str(A0)) #Update label with next text.

    root.after(1000, update_label)
    #calls update_label function again after 1 second. (1000 milliseconds.)


root = ttk.Tk()
root.geometry('500x400')
root.geometry

#Static Labels
ohmLabel = ttk.Label(
    root,
    text = "Resistance"
).grid(
    column = 0
)

tickLabel = ttk.Label( #Lables tick counter
    root,
    text = "Ticks:",
    font = (bigFont)
).grid(
    column = 0,
    row = 0
)

timeLabel = ttk.Label( #Lables time counter
    root,
    text = "Time:",
    font = (bigFont)
).grid(
    column = 0,
    row = 2
)

#Output Labels
ohmCounter = ttk.Label(
    root,
    text = "" 
).grid(
    column = 0,
    row = 1
)

tickCounter = ttk.Label( #Outputs incoming tick count
    root,
    text = ""
).grid(
    column = 0,
    row = 1
)

timeCounter = ttk.Label( #Outputs calculated time
    root,
    text = "",
    font = (22)
).grid(
    column = 0,
    row = 3
)




root.grid
root.mainloop()
