from tkinter import *
from tkinter import filedialog as fd
import pyttsx3
import webbrowser

engine = pyttsx3.init()



c = Tk()

c.geometry("%dx%d" % (c.winfo_screenwidth(),c.winfo_screenheight()))

text1 = Text(c,width=158,height=48)
text1.place(x=250,y=5)

def auto():
    e = Frame(c,width=400,height=250,bg="#283747")
    e.place(x=600,y=270)

    Label(e,text="This App can only read txt files, so if you have a non-txt file,",font=(NORMAL,11),bg="#283747",fg="white").place(x=5,y=5)
    Label(e,text="you must convert it to txt.",font=(NORMAL,11),bg="#283747",fg="white").place(x=5,y=25)
    Label(e,text="Here are some free websites to convert your txt file:",font=(NORMAL,11),bg="#283747",fg="white").place(x=5,y=45)

    def links1():
        webbrowser.open("https://cloudconvert.com/txt-converter")

    def links2():
        webbrowser.open("https://convertio.co/de/")

    def links3():
        webbrowser.open("https://dokument.online-convert.com/de/umwandeln-in-txt")

    def links4():
        webbrowser.open("https://www.zamzar.com/converters/document/txt/")

    def links5():
        webbrowser.open("https://anyconv.com/de/txt-konverter/")

    link1 = Button(e,text="https://cloudconvert.com/txt-converter",width=30,height=1,bg="#34495E",fg="white",command=links1)
    link1.place(x=5,y=190)

    link2 = Button(e,text="https://convertio.co/de/",width=30,height=1,bg="#34495E",fg="white",command=links2)
    link2.place(x=5,y=160)

    link3 = Button(e,text="https://dokument.online-convert.com/de/umwandeln-in-txt",width=50,height=1,bg="#34495E",fg="white",command=links3)
    link3.place(x=5,y=130)

    link4 = Button(e,text="https://www.zamzar.com/converters/document/txt/",width=50,height=1,bg="#34495E",fg="white",command=links4)
    link4.place(x=5,y=100)

    link5 = Button(e,text="https://anyconv.com/de/txt-konverter/",width=50,height=1,bg="#34495E",fg="white",command=links5)
    link5.place(x=5,y=70)
    def ok1():
        e.destroy()


    ok = Button(e,text="Ok",width=10,height=1,bg="#34495E",fg="white",command=ok1)
    ok.place(x=310,y=220)

auto()


def file():
    filename = fd.askopenfilename(filetypes=(("All files", "*.*"),("Text files", "*.txt"),("PDF files", "*.pdf")))

    text1.delete("1.0",END)

    f = open(filename,"r")
    file_contents = f.read()
    f.close()
    text1.insert("1.0",file_contents)


prev_input = ''

def read():
    text = text1.get("1.0", END)
    engine.say(text)
    engine.runAndWait()


lesen = Button(c,text="Reading",width=10,height=1,font=(NORMAL,30),bg="#34495E",fg="white",command=read)
lesen.place(x=2,y=95)

fiel = Button(c,text="Load a file",width=10,height=1,font=(NORMAL,30),bg="#34495E",fg="white",command=file)
fiel.place(x=2,y=5)

ficr1 = Button(c,text="File converter",width=10,height=1,font=(NORMAL,30),bg="#34495E",fg="white",command=auto)
ficr1.place(x=2,y=185)


c.mainloop()

