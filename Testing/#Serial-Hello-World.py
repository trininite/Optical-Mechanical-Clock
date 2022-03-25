#Serial Test 1
from turtle import update
import serial
import time
from tkinter import * 
import tkinter as ttk
import threading

ser = serial.Serial('/dev/ttyACM0', 9600)
clk = 0




def update_label():
    data = ser.readline().decode("utf-8")
    output.config(text = str(data))

def update_label():
    data = float(ser.readline())

    output.config(text=str(data)) #Update label with next text.

    root.after(1000, update_label)
    #calls update_label function again after 1 second. (1000 milliseconds.)


root = ttk.Tk()
#root.geometry("100x100")

output = ttk.Label(
    root,
    text = "Text"
)

updateButton = ttk.Button(
    root,
    text = "Update",
    command = update_label
)


output.pack(padx = 100, pady = 100)
updateButton.pack(padx = 100, pady = 100)

root.mainloop()


     
#data = ser.readline().decode("utf-8")