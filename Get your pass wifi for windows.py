import os
from tkinter import *



v = Tk()
v.geometry("600x400")
v.config(bg="#28343B")
#v.resizable(False,False)


def wifi():
    d = """netsh wlan show profile name="FRITZ!Box 7590 HE" key=clear"""
    p = os.popen(d)
    s = p.read()
    p.close()

    os.chdir(r"C:\\")
    with open("ou.txt", "w") as file:
        file.write(s)

    with open(r"C:\ou.txt", "r") as file:
        lines = file.readlines()

    with open(r"C:\ou.txt", "w") as file:
        for i, line in enumerate(lines):
            if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                         26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]:
                file.write(line)

    with open(r"C:\ou.txt", "r") as file:
        content = file.read()
        print(content)



        la = Label(v,text=content,font=3)
        la.place(x=-10,y=150)

        pa = Frame(width=205,height=250,bg="#28343B")
        pa.place(x=0,y=0)

        la = Label(v, text="Your wifi pass is :", font=(5))
        la.place(x=235, y=100)


    os.remove(r"C:\ou.txt")


get = Button(v,text="Get",width=30,height=3,command=wifi)
get.place(x=200,y=300)


v.mainloop()

