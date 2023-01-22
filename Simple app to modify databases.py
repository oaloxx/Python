from tkinter import *
import sqlite3
from tkinter import messagebox

with sqlite3.connect("details.db") as db:
    curses = db.cursor()

curses.execute("""CREATE TABLE IF NOT EXISTS users0(id integer PRIMARY KEY AUTOINCREMENT,
username text NOT NULL,password text NOT NULL);""")



def add_new_user():
    newUsername = username.get()
    newPassword = password.get()

    curses.execute("delete from users0 where id=2")

    curses.execute("SELECT COUNT(*) from users0 WHERE username = '" + newUsername + "' ")
    result = curses.fetchone()

    if int(result[0]) > 0:
        messagebox.showerror("Username", "Error: Username already exists")



    else:

        curses.execute("INSERT INTO users0(username,password)VALUES(?,?)", (newUsername, newPassword))
        db.commit()
        fetch_all_data()



win = Tk()
win.geometry("850x380")
win.resizable(False, False)
win.title("Modify databases")

Label3 = Label(win, text="Enter User id to delete")
Label3.place(x=10, y=120)
user_id_entry = Entry()
user_id_entry.place(x=150, y=120, width=200, height=25)


def add_new_users():
    user_id = user_id_entry.get()
    curses.execute("delete from users0 where id=" + user_id)
    db.commit()
    fetch_all_data()



def fetch_all_data():
    textbox.delete(1.0, END)
    curses.execute("SELECT * from users0")
    result = curses.fetchall()
    data = ""
    for row in result:
        data += str(row) + "\n"
    textbox.insert(INSERT, data)


def update_user():
    Label12s = Label(win, text="Enter the ID user to edit")
    Label12s.place(x=10, y=200)

    u = Entry(win)
    u.place(x=150, y=200, width=200, height=25)

    Label12s1 = Label(win, text="Enter to edit username")
    Label12s1.place(x=10, y=240)

    u1 = Entry(win)
    u1.place(x=150, y=240, width=200, height=25)

    Label12s2 = Label(win, text="Enter to edit password")
    Label12s2.place(x=10, y=280)

    u2 = Entry(win)
    u2.place(x=150, y=280, width=200, height=25)

    def save():
        curses.execute("UPDATE users0 SET username = ?, password = ? WHERE id = ?", (u1.get(), u2.get(), u.get()))
        db.commit()
        fetch_all_data()

    botton_ok = Button(text="Save", command=save)
    botton_ok.place(x=10, y=330, width=175, height=45)
    fetch_all_data()



def clear():
    textbox.delete(1.0, END)



textbox = Text(win)
textbox.place(x=400, y=10, width=420, height=350)

Label1 = Label(win, text="Enter new Username")
Label1.place(x=10, y=10)

Label12 = Label(win, text="Enter new Password")
Label12.place(x=10, y=50)

username = Entry()
username.place(x=150, y=10, width=200, height=25)

password = Entry()
password.place(x=150, y=50, width=200, height=25)


bottonx = Button(text="Add", command=add_new_user)
bottonx.place(x=90, y=80, width=75, height=35)

bottonxc = Button(text="Clear", command=clear)
bottonxc.place(x=170, y=80, width=75, height=35)

botton1 = Button(text="Fetch", command=fetch_all_data)
botton1.place(x=10, y=80, width=75, height=35)

botton = Button(text="Delete", command=add_new_users)
botton.place(x=10, y=150, width=75, height=35)

botton = Button(text="Update (Modification)", command=update_user)
botton.place(x=90, y=150, height=35)

win.mainloop()
