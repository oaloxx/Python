from tkinter import *
from pytube import YouTube
import os
import tkinter.filedialog as filedialog

x = Tk()
x.geometry("600x400")
x.title("youtube MP3 downloader")
sx = Frame(x, width=600, height=400, bg="#1B90CA")
sx.place(x=0, y=0)

linkx = StringVar()

ex = Entry(sx, width=85, textvariable=linkx)
ex.place(x=80, y=255)
Label(text="youtube MP3 downloader", font=(1), bg="#1B90CA", fg="white").place(x=5, y=5)

Label(sx,text="if the download takes a lot of time, please check that the link is \n correct                                                                                ",font=2, bg="#1B90CA", fg="white").place(x=1,y=200)

Label(sx,text="ctrl + v = Paste",font=2).place(x=1,y=130)
Label(sx,text="ctrl + c = Copy ",font=2).place(x=1,y=160)

def downloaderx():

    url=YouTube(str(linkx.get()))
    video=url.streams.filter(only_audio=True).first()

    file_path = filedialog.asksaveasfilename(title='Save Video', defaultextension='.mp4')

    out_file = video.download(output_path=file_path)

    base,ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)



l = Label(sx, text="URL =", font=(1), bg="#1B90CA",fg="white")
l.place(x=5, y=250)


b = Button(sx,text="Download",width=50,height=2,font=(1),command=downloaderx,bg="#1F5D97",fg="white")
b.place(x=20,y=300)

x.mainloop()
