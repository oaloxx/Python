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

def blackss(evevt):
  color="black"
  x1,y1=(evevt.x-2000) , (evevt.y-2000)
  x2, y2 = (evevt.x + 2000), (evevt.y + 2000)
  c.create_oval (x1,y1,x2,y2,fill=color,outline=color)

master = Tk()
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
  c.delete("all")





red1 = Button(master,width=4,height=2,bg="red",command=reda)
red1.place(y=360,x=15)

blue2 = Button(master,width=4,height=2,bg="blue",command=bluea)
blue2.place(y=310,x=60)

black3 = Button(master,width=4,height=2,bg="black",command=blacka)
black3.place(y=110,x=15)

green4 = Button(master,width=4,height=2,bg="green",command=greena)
green4.place(y=110,x=60)

yellow5 = Button(master,width=4,height=2,bg="yellow",command=yellowa)
yellow5.place(y=160,x=15)

white6 = Button(master,width=4,height=2,bg="white",command=whitea)
white6.place(y=160,x=60)

orange7 = Button(master,width=4,height=2,bg="orange",command=orangea)
orange7.place(y=210,x=15)

purple8 = Button(master,width=4,height=2,bg="purple",command=purplea)
purple8.place(y=210,x=60)

brown9 = Button(master,width=4,height=2,bg="brown",command=browna)
brown9.place(y=260,x=15)

gray10 = Button(master,width=4,height=2,bg="gray",command=graya)
gray10.place(y=260,x=60)

pink11 = Button(master,width=4,height=2,bg="pink",command=pinka)
pink11.place(y=310,x=15)

eraser = Button(master,width=10,height=2,text="Eraser",command=whitea)
eraser.place(y=60,x=20)

b5 = Button(master,text="clear all",width=10,height=2,command=clear)
b5.place(x=20,y=5)



c = Canvas(master,width=1500,height=800,bg="white")
c.place(x=120,y=0)
c.bind("<B1-Motion>",paint)

master.mainloop()

