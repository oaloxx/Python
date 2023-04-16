import tkinter as tk
from tkinter import filedialog
import pygame
from tkinter import *
import os
from pygame import mixer
#

def play_music():
    currentsong = playlist.get(ACTIVE)
    mixer.music.load(currentsong)
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

def choose_music_file():
    global directory_path
    aso.destroy()
    directory_path = filedialog.askdirectory()
    os.chdir(directory_path)
    songs = [s for s in os.listdir(directory_path) if s.endswith(('.mp3', '.wav', '.ogg', '.acc', '.flac', '.aiff', '.wma', '.wma', '.dsd', '.ac3'))]
    playlist.delete(0, END)
    for s in songs:
        playlist.insert(END, s)

pygame.mixer.init()

root = tk.Tk()
root.title("Music Player")
root.geometry("507x260")
root.resizable(False,False)



playlist = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), width=30,height=11)
playlist.place(x=175,y=0)



play_button = tk.Button(root, text="Play",font=(3),width=15,height=2, command=play_music)
pause_button = tk.Button(root, text="Pause",font=(3),width=15,height=2, command=pause_music)
stop_button = tk.Button(root, text="Stop",font=(3),width=15,height=2, command=stop_music)
choose_button = tk.Button(root, text="Choose yore \n music folder",font=(3),width=15,height=2, command=choose_music_file)

play_button.place(x=0,y=0)
pause_button.place(x=0,y=65)
stop_button.place(x=0,y=130)
choose_button.place(x=0,y=195)


aso = Label(root,text="Music folder is not selected")
aso.place(x=270,y=110)

root.mainloop()
