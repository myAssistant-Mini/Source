# This is the main file . Execution starts here. Run this file in IDE

from tkinter import *

import tkinter as tk
from tkvideo import tkvideo

from mini import open_mini

root = Tk()
my_label = Label(root)
my_label.pack()

# player = tkvideo("C:\\Users\\acer\\PycharmProjects\\myAssistant-Mini\\mm.mp4",  my_label, loop=1, size=(400, 700))  # Atharva's
player = tkvideo("C:\\Users\\admin\\Desktop\\Vs Code Python\\mm.mp4", my_label, loop=1, size=(300, 500)) # Bhavesh's
# Simply comment out the user as per your need for the path :)

start = tk.Button(root, text="myAssistant", command=open_mini)

start.pack()
player.play()

root.mainloop()
