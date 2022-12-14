from tkinter import *
import random

f = Tk()
f.geometry("600x400")
f.resizable(False,False)
f.title("H W M(Rock-Paper-Scissors game)")
x = Frame(f, bg="#0F1F30", width=10000, height=100000)
x.place(x=0, y=0)



zlfc = int(0)
zlfp = int(0)


def wider():
    global zlfp
    global zlfc
    zlfc = int(0)
    zlfp = int(0)

    global b1
    global b2
    global b3

    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"

    b1 = Button(x, font=(9), text="H", width=18, height=6, command=h, bg="black", fg="#FFFFFF")
    b1.place(x=1, y=260)
    b2 = Button(x, font=(9), text="W", width=18, height=6, bg="black", fg="#FFFFFF", command=w)
    b2.place(x=210, y=260)
    b3 = Button(x, font=(9), text="M", width=16, height=6, bg="black", fg="#FFFFFF", command=m)
    b3.place(x=419, y=260)

    l7 = Label(x, font=(9), text=f"P = 0")
    l7.place(x=5, y=20)
    l8 = Label(x, font=(9), text=f"C = 0")
    l8.place(x=5, y=60)

    l9 = Label(x, font=(9), text=f"C = ")
    l9.place(x=5, y=115)

    l10 = Label(x, font=(9), text=f"D = ")
    l10.place(x=5, y=155)









def weite():



    global b1
    global b2
    global b3

    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"

    b1 = Button(x, font=(9), text="H", width=18, height=6, command=h, bg="black", fg="#FFFFFF")
    b1.place(x=1, y=260)
    b2 = Button(x, font=(9), text="W", width=18, height=6, bg="black", fg="#FFFFFF", command=w)
    b2.place(x=210, y=260)
    b3 = Button(x, font=(9), text="M", width=16, height=6, bg="black", fg="#FFFFFF", command=m)
    b3.place(x=419, y=260)


    l9 = Label(x, font=(9), text=f"C = ")
    l9.place(x=5, y=115)


    global l1
    l1.destroy()

    l5 = Label(x,bg="#0F1F30", text="                                                                                    ", font=(6))
    l5.place(x=5, y=220)
    l4 = Label(x,bg="#0F1F30", text="                                                                                    ", font=(6))
    l4.place(x=5, y=220)
    l6 = Label(x,bg="#0F1F30", text="                                                                                    ", font=(6))
    l6.place(x=5, y=220)

    l101 = Label(x,bg="#0F1F30", font=(9), text="    ")
    l101.place(x=47, y=155)
    l102 = Label(x,bg="#0F1F30", font=(9), text="    ")
    l102.place(x=47, y=155)
    l103 = Label(x,bg="#0F1F30", font=(9), text="    ")
    l103.place(x=47, y=155)




    l7 = Label(x, font=(9), text=f"P = {zlfp}")
    l7.place(x=5, y=20)
    l8 = Label(x, font=(9), text=f"C = {zlfc}")
    l8.place(x=5, y=60)



def h():
    global op
    global p
    op = ["m", "w", "h"]
    p = random.choice(op)
    print(p)
    global b1
    global b2
    global b3
    global l1
    global l4
    global l5
    global l6
    global l101

    l101 = Label(x, font=(9), text=f"D = h ")
    l101.place(x=5, y=155)

    if p == "w":
        global l4
        global l5
        global l6
        global l1
        l4 = Label(x, text="-                   Computer hat gewohnen                           -", font=(6))
        l4.place(x=5, y=220)

        l1 = Label(x, font=(9), text=f"C = {p}")
        l1.place(x=5, y=115)



        b4 = Button(x, font=(2), text="weiter", command=weite)
        b4.place(x=520, y=170)

        global zlfc

        zlfc += int(1)
        l2 = Label(x, font=(9), text=f"C = {zlfc}")
        l2.place(x=5, y=60)

        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"
        b3["state"] = "disable"
    if p == "h":

        l5 = Label(x, text="Ihr beide haben gleich ergebnes, bitte widerholen", font=(6))
        l5.place(x=5, y=220)

        l1 = Label(x, font=(9), text=f"C = {p}")
        l1.place(x=5, y=115)

        b4 = Button(x, font=(2), text="weiter", command=weite)
        b4.place(x=520, y=170)

        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"

    if p == "m":

        l6 = Label(x, text="-                     Du hats gewohnen                          -", font=(6))
        l6.place(x=5, y=220)

        global zlfp

        zlfp += int(1)

        l3 = Label(x, font=(9), text=f"P = {zlfp}")
        l3.place(x=5, y=20)

        l1 = Label(x, font=(9), text=f"C = {p}")
        l1.place(x=5, y=115)

        b4 = Button(x, font=(2), text="weiter", command=weite)
        b4.place(x=520, y=170)

        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"


def w():
    global op
    global p
    op = ["m", "w", "h"]
    p = random.choice(op)
    print(p)
    global b1
    global b2
    global b3
    global l102
    global l1

    l102 = Label(x, font=(9), text=f"D = w")
    l102.place(x=5, y=155)

    if p == "w":

        l4 = Label(x, text="ihr beide haben gleich ergebnes, bitte widerholen", font=(6))
        l4.place(x=5, y=220)

        l1 = Label(x, font=(9), text=f"C = {p}")
        l1.place(x=5, y=115)

        b4 = Button(x, font=(2), text="weiter", command=weite)
        b4.place(x=520, y=170)

        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"

    if p == "h":

        l5 = Label(x, text="-                    Du bist gewohnen                        -", font=(6))
        l5.place(x=5, y=220)

        l1 = Label(x, font=(9), text=f"C = {p}")
        l1.place(x=5, y=115)

        b4 = Button(x, font=(2), text="weiter", command=weite)
        b4.place(x=520, y=170)

        global zlfp

        zlfp += int(1)
        l2 = Label(x, font=(9), text=f"P = {zlfp}")
        l2.place(x=5, y=20)

        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"

    if p == "m":

        l6 = Label(x, text="-                    Computer hat gewohnen                        -", font=(6))
        l6.place(x=5, y=220)
        global zlfc

        zlfc += int(1)
        l2 = Label(x, font=(9), text=f"C = {zlfc}")
        l2.place(x=5, y=60)

        l1 = Label(x, font=(9), text=f"C = {p}")
        l1.place(x=5, y=115)

        b4 = Button(x, font=(2), text="weiter", command=weite)
        b4.place(x=520, y=170)

        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"


def m():
    global op
    global p
    op = ["m", "w", "h"]
    p = random.choice(op)
    print(p)

    global b1
    global b2
    global b3

    global l1
    global l103

    l103 = Label(x, font=(9), text=f"D = m ")
    l103.place(x=5, y=155)


    if p == "w":

        l4 = Label(x, text="-                    Du bist gewohnen                         -", font=(6))
        l4.place(x=5, y=220)

        l1 = Label(x, font=(9), text=f"C = {p}")
        l1.place(x=5, y=115)

        b4 = Button(x, font=(2), text="weiter", command=weite)
        b4.place(x=520, y=170)

        global zlfp

        zlfp += int(1)
        l2 = Label(x, font=(9), text=f"P = {zlfp}")
        l2.place(x=5, y=20)

        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"

    if p == "h":

        l5 = Label(x, text="-                    Computer hat gewohnen                          -", font=(6))
        l5.place(x=5, y=220)

        l1 = Label(x, font=(9), text=f"C = {p}")
        l1.place(x=5, y=115)

        b4 = Button(x, font=(2), text="weiter", command=weite)
        b4.place(x=520, y=170)

        global zlfc

        zlfc += int(1)
        l2 = Label(x, font=(9), text=f"C = {zlfc}")
        l2.place(x=5, y=60)

        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"

    if p == "m":

        l6 = Label(x, text="ihr beide haben gleich ergebnes, bitte widerholen", font=(6))
        l6.place(x=5, y=220)

        l1 = Label(x, font=(9), text=f"C = {p}")
        l1.place(x=5, y=115)

        b4 = Button(x, font=(2), text="weiter", command=weite)
        b4.place(x=520, y=170)

        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"


global l1
global l4
global l5
global l6

b1 = Button(x, font=(9), text="H", width=18, height=6, command=h, bg="black", fg="#FFFFFF")
b1.place(x=1, y=260)
b2 = Button(x, font=(9), text="W", width=18, height=6, bg="black", fg="#FFFFFF", command=w)
b2.place(x=210, y=260)
b3 = Button(x, font=(9), text="M", width=16, height=6, bg="black", fg="#FFFFFF", command=m)
b3.place(x=419, y=260)

l7 = Label(x, font=(9), text=f"P = 0")
l7.place(x=5, y=20)
l8 = Label(x, font=(9), text=f"C = 0")
l8.place(x=5, y=60)
l9 = Label(x, font=(9), text=f"C = ")
l9.place(x=5, y=115)
l10 = Label(x, font=(9), text=f"D = ")
l10.place(x=5,y=155)
b5 = Button(x, font=(2), text=" wider",command=wider)
b5.place(x=520, y=210)

def qq():
    q = Tk()
    q.geometry("400x400")
    q.resizable(False,False)
    q.title("??")
    Label(q,font=3,text="P = Player(Punkte)").place(x=5,y=5)
    Label(q, font=3, text="C = Computer(Punkte)").place(x=5, y=45)
    Label(q, font=3, text="C = Was der Computer gewahlt hat").place(x=5, y=110)
    Label(q, font=3, text="D = Was du gewahlt hast ").place(x=5, y=155)

    Label(q, font=3, text="H = Rock").place(x=5, y=250)
    Label(q, font=3, text="W = Paper").place(x=5, y=300)
    Label(q, font=3, text="S = Scissors").place(x=5, y=350)

    q.mainloop()

Button(x,text="??",font=2,width=4,command=qq).place(x=540,y=5)

f.mainloop()

