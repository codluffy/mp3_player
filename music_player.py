import pygame 
from pygame import mixer 
from tkinter import StringVar, Tk, Label, Listbox, Button 
from tkinter import ACTIVE, SINGLE 
from tkinter.filedialog import askdirectory 
import os 

FONT = ("Consolas 12 bold")
X = 0
VER = '1.2.2'   # not-defalut

player = Tk() 
player.title(f"Music Player: {VER}")
player.geometry("270x300")  # player.resizable(0, 0)

var = StringVar()
var.set("Select the song to play")

os.chdir(askdirectory()) 
songlist = os.listdir()

playing = Listbox(player, font=FONT, width=28, bg="black", fg="white", selectmode=SINGLE)

for item in songlist:
    playing.insert('end', item) 

pygame.init()
mixer.init()


def Play():
        mixer.music.load(playing.get(ACTIVE))
        name = playing.get(ACTIVE)
        var.set(f"{name[:16]}..." if len(name)>18 else name)
        mixer.music.play()


def Mute():
    global X
    if X%2==0:
        mixer.music.pause()
    if X%2==1:
        mixer.music.unpause()
    X += 1


def Quit():
    mixer.music.stop()
    exit()


text = Label(player, font=FONT, textvariable=var)
text.grid(row=0, columnspan=3)
playing.grid(columnspan=3)

playB =Button(player, width=8, height=1, font=FONT, text="Play", command=Play, bg="lightgreen")
playB.grid(row=2, column=0)
pauseB= Button(player, width=8, height=1, font=FONT, text="Mute", command=Mute, bg="lightblue", fg="black")
pauseB.grid(row=2, column=1)
resumeB = Button(player, width=9, height=1, font=FONT, text="Exit", command=Quit, bg="lightpink", fg="black")
resumeB.grid(row=2, column=2)

player.mainloop()
