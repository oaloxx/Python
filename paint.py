from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import *



def paint(evevt):
  color="blue"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def red(evevt):
  color="red"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def blue(evevt):
  color="blue"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def black(evevt):
  color="black"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def green(evevt):
  color="green"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def yellow(evevt):
  color="yellow"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def white(evevt):
  color="white"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def orange(evevt):
  color="orange"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def purple(evevt):
  color="purple"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def brown(evevt):
  color="brown"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def gray(evevt):
  color="gray"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def pink(evevt):
  color="pink"
  x1,y1=(evevt.x-11) , (evevt.y-11)
  x2, y2 = (evevt.x + 11), (evevt.y + 11)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

def whitees(evevt):
  color="white"
  x1,y1=(evevt.x-2000) , (evevt.y-2000)
  x2, y2 = (evevt.x + 2000), (evevt.y + 2000)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

master = Tk()
master.title("Beginner paint")
def reda():
  c.bind("<B1-Motion>",red)

def bluea():
    c.bind("<B1-Motion>", blue)

def blacka():
  c.bind("<B1-Motion>", black)

def greena():
  c.bind("<B1-Motion>", green)

def yellowa():
  c.bind("<B1-Motion>", yellow)

def whitea():
  c.bind("<B1-Motion>", white)

def orangea():
  c.bind("<B1-Motion>", orange)

def purplea():
  c.bind("<B1-Motion>", purple)

def browna():
  c.bind("<B1-Motion>", brown)

def graya():
  c.bind("<B1-Motion>", gray)

def pinka():
  c.bind("<B1-Motion>", pink)

def clear():
  c.bind("<B1-Motion>", whitees)


f = Frame(master,width=60,height=700,bg="white")
f.place(x=20,y=50)

red1 = Button(f,width=4,height=2,bg="red",command=reda)
red1.place(y=7,x=15)

blue2 = Button(f,width=4,height=2,bg="blue",command=bluea)
blue2.place(y=60,x=15)

black3 = Button(f,width=4,height=2,bg="black",command=blacka)
black3.place(y=115,x=15)

green4 = Button(f,width=4,height=2,bg="green",command=greena)
green4.place(y=170,x=15)

yellow5 = Button(f,width=4,height=2,bg="yellow",command=yellowa)
yellow5.place(y=225,x=15)

white6 = Button(f,width=4,height=2,bg="white",command=whitea)
white6.place(y=280,x=15)

orange7 = Button(f,width=4,height=2,bg="orange",command=orangea)
orange7.place(y=340,x=15)

purple8 = Button(f,width=4,height=2,bg="purple",command=purplea)
purple8.place(y=400,x=15)

brown9 = Button(f,width=4,height=2,bg="brown",command=browna)
brown9.place(y=455,x=15)

gray10 = Button(f,width=4,height=2,bg="gray",command=graya)
gray10.place(y=510,x=15)

pink11 = Button(f,width=4,height=2,bg="pink",command=pinka)
pink11.place(y=570,x=15)

b5 = Button(master,text="clear",width=10,height=2,command=clear)
b5.place(x=20,y=5)

l1 = Label(master,text="for to use clear press <clear> then press of any area and move the mouse on master ",font=2)
l1.place(x=100,y=10)


c = Canvas(master,width=1500,height=800,bg="white")
c.place(x=100,y=50)
c.bind("<B1-Motion>",paint)







master.mainloop()


