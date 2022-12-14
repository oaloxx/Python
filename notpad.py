from tkinter.filedialog import *
from tkinter import *

def saveFile():
    new_file = asksaveasfile(mode="w",filetypes=[("text files",".txt")])
    if new_file is None:
        return
    text = str(entry.get(1.0,END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode="r",filetypes=[("text files","*.txt")])
    if file is not None:
        content = file.read()
    entry.insert(INSERT,content)

def clearFile():
    entry.delete(1.0,END)

ca = Tk()
ca.geometry("400x600")
ca.config(bg="black")

top = Frame(ca)
top.pack(padx=10,pady=5,anchor="nw")

b1=Button(ca,text="Open",bg="white",command=openFile)
b1.pack(in_=top,side=LEFT)

b2=Button(ca,text="save",bg="white",command=saveFile)
b2.pack(in_=top,side=LEFT)

b3=Button(ca,text="clear",bg="white",command=clearFile)
b3.pack(in_=top,side=LEFT)

b4=Button(ca,text="Exit",bg="white",command=exit)
b4.pack(in_=top,side=LEFT)

entry = Text(ca,wrap= WORD,font=(15),bg="#17202A",fg="white")
entry.pack(padx=10,pady=5,expand=TRUE,fill=BOTH)

ca.mainloop()
