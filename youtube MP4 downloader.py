from tkinter import *
from pytube import YouTube
import tkinter.filedialog as filedialog


a = Tk()
a.geometry("600x400")
a.title("MP4 youtube downloader")
a.resizable(False,False)
s = Frame(a,width=600,height=400,bg="#1B90CA")
s.place(x=0,y=0)

link = StringVar()

e = Entry(a,width=85,textvariable = link)
e.place(x=80,y=255)
Label(text="MP4 youtube downloader",font=(1),bg="#1B90CA",fg="white").place(x=5,y=5)

Label(s,text="ctrl + v = Paste",font=2).place(x=1,y=130)
Label(s,text="ctrl + c = Copy ",font=2).place(x=1,y=160)

Label(s,text="if the download takes a lot of time, please check that the link is \n correct                                                                                ",font=2, bg="#1B90CA", fg="white").place(x=1,y=200)
def downloader():

    url=YouTube(str(link.get()))
    video=url.streams.get_highest_resolution()
    global asy1
    global asy2


    file_path = filedialog.asksaveasfilename(title='Save Video', defaultextension='.mp4')
    video.download(file_path)

l = Label(s,text="URL =",font=(1),bg="#1B90CA",fg="white")
l.place(x=5,y=250)
b = Button(s,text="Download",width=50,height=2,font=(1),command=downloader,bg="#1F5D97",fg="white")
b.place(x=20,y=300)


a.mainloop()
