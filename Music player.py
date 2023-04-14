from pygame import mixer 
from tkinter import *

root=Tk()
root.geometry("600x300")

mixer.init()
mixer.music.load("Diviners X Riell - Slow [NCS Release].mp3")

def pause():
    mixer.music.pause()

def play():
    mixer.music.play()

def resume():
    mixer.music.unpause()

Label(root, text= "Welcome to Priyansh's Music Player",font= "lucidia 30 bold").pack()
Button(text="Play", command=play).place(x=100,y=100)
Button(text="Pause", command=pause).place(x=200,y=100)
Button(text="Resume", command=resume).place(x=300,y=100)
Button(text="Quit", command=quit).place(x=400,y=100)

root.mainloop()