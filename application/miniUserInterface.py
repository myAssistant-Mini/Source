# This is the main file . Execution starts here. Run this file in IDE

#DOWNLOAD IMAGES AND GUI.MP4 FROM SRC

import pygame
from pygame import mixer

from tkinter import *
import tkinter as tk
from tkvideo import tkvideo

from mini import open_mini,open_search

pygame.init()
mixer.music.load('song.mp3')
mixer.music.play(0)

root = Tk()
root.title('MINI Search Engine')
p1 = PhotoImage(file='favicon.png')
root.iconphoto(False, p1)
my_label = Label(root)
my_label.pack()
player = tkvideo("C:\\Users\\acer\\PythonProjects\\myAssistant-Mini\\gui.mp4",
                 my_label, loop=1, size=(400, 700))
# player = tkvideo("C:\\Users\\admin\\Desktop\\Vs Code Python\\gui.mp4", my_label, loop=1, size=(300, 500)) # Bhavesh's 
start = tk.Button(root, text="myAssistant", command=open_mini)
start.pack(side=LEFT)
search = tk.Button(root, text="mySearch", command=open_search)
search.pack(side=RIGHT)
player.play()

root.mainloop()
