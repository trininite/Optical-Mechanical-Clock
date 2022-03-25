#Main

from tkinter import *
import tkinter as ttk
import time

root = Tk
root.geometry("500x500")

#Static Labels
tickLabel = ttk.Label(
    root,
    text = "Ticks:"
)

timeLabel = ttk.Label(
    root,
    text = "Time:"
)

#Output Labels
tickCount = ttk.Label(
    root,
    text = ""
)

timeCount = ttk.Label(
    root,
    text = ""
)









root.grid()

root.mainloop()
