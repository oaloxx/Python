from tkinter import *
from datetime import date


today = date.today()


o = Tk()
o.geometry("300x350")
o.resizable(False,False)

def only_numbers(char):
    return char.isdigit()

validation = o.register(only_numbers)

y = Frame(o,bg="#85C1E9",width=1150,height=40).place(x=0,y=0)
a1 = Entry(y,width=20, validate="key", validatecommand=(validation, '%S'))
a1.place(x=150,y=10)
a1.insert(0,0)
Label(y,text="The year",font=2,bg="#85C1E9").place(x=10,y=5)

y1 = Frame(o,bg="#5DADE2",width=1150,height=40).place(x=0,y=40)
a2 = Entry(y1,width=20, validate="key", validatecommand=(validation, '%S'))
a2.place(x=150,y=50)
a2.insert(0,0)
Label(y1,text="The month",font=2,bg="#5DADE2").place(x=10,y=45)

y3 = Frame(o,bg="#3498DB",width=1150,height=40).place(x=0,y=80)
a3 = Entry(y3,width=20, validate="key", validatecommand=(validation, '%S'))
a3.place(x=150,y=90)
a3.insert(0,0)
Label(y3,text="The day",font=2,bg="#3498DB").place(x=10,y=83)

f1 = Frame(o,bg="#A2D9CE",width=1111,height=170).place(y=120,x=0)



def ca():
    yx = int(a1.get())
    b = yx - today.year

    yx1 = int(a2.get())
    c = yx1 - today.month

    yx2 = int(a3.get())
    d = yx2 - today.day


    Label(f1,text=f"{b}              ",font=2,bg="#A2D9CE").place(y=130,x=-7)
    Label(f1, text="year", font=2,bg="#A2D9CE").place(y=127, x=60)
    Label(f1, text=f"{c}               ", font=2,bg="#A2D9CE").place(y=160, x=0)
    Label(f1, text="month", font=2,bg="#A2D9CE").place(y=158, x=60)
    Label(f1, text=f"{d}                ", font=2,bg="#A2D9CE").place(y=190, x=0)
    Label(f1, text="day", font=2,bg="#A2D9CE").place(y=187, x=60)





b1 = Button(o,text="Calculate",bg="#58D68D",font=2,width=25,height=0,command=ca).place(x=7,y=300)

o.mainloop()


