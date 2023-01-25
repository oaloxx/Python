from tkinter import *
from tkinter import filedialog as fd
import tkinter.filedialog as filedialog


a = Tk()
a.geometry("400x200")
a.resizable(False,False)
a.title("Choose a video to convert to audio")

s = Frame(a,width=600,height=400,bg="#1B90CA")
s.place(x=0,y=0)

def downloader():
    filename = fd.askopenfilename()

    from moviepy.video.io.VideoFileClip import VideoFileClip
    clip = VideoFileClip(filename)

    Label(a, text="Please wait form 5 to 20 second", font=(3)).place(x=0, y=160)

    file_path = filedialog.asksaveasfilename(title='Save Video', defaultextension='.mp3')
    clip.audio.write_audiofile(file_path)


b = Button(s,text="Choose a video to convert to audio",command=downloader,bg="#1F5D97",fg="white",width=30,height=3,font=(0))
b.place(x=30,y=59)

a.mainloop()