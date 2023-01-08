from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class Database:
    def __init__(self,l):
        self.con = sqlite3.connect(l)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            job text,
            email text,
            gender text,
            mobile text,
            address text

        )
        """
        self.con.execute(sql)  # sql ran
        self.con.commit()

    def insert(self, name, age, job, email, gender, mobile, address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                         (name, age, job, email, gender, mobile, address))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("delete from employees where id=?", (id,))
        self.con.commit()

    def update(self, id, name, age, job, email, gender, mobile, address):
        self.cur.execute("Update employees set name=?,age=?,job=?,email=?,gender=?,mobile=?,address=? where id=?",
                         (name, age, job, email, gender, mobile, address, id))
        self.con.commit()


data_sql = Database("Employee.data_sql")

###########################################################################################################################################

root = Tk()
root.title("Employee Management system")
root.config(bg="#2c3e50")
root.resizable(True,True)
width= root.winfo_screenwidth()
height= root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))



name = StringVar()
age = StringVar()
job = StringVar()
gender = StringVar()
email = StringVar()
mobile = StringVar()

#xd = PhotoImage(r"C:\Users\Moham\Desktop\sxc.jpg")
#sa = Label(image=xd)
#sa.place(x=80,y=520)





#====== Entries Farme=======

entries_farme = Frame(root,bg="#2c3e50")
entries_farme.place(x=1,y=1,width=360,height=510)
title = Label(entries_farme,text="Employee Comany",font=(18),bg="#2c3e50",fg="white")
title.place(x=1,y=1)

lbName = Label(entries_farme,text="Name",font=(16),bg="#2c3e50",fg="white")
lbName.place(x=10,y=50)
txName = Entry(entries_farme,textvariable=name ,width=20,font=(16))
txName.place(x=120,y=50)

lbljob = Label(entries_farme,text="Job",font=(16),bg="#2c3e50",fg="white")
lbljob.place(x=10,y=90)
txjob = Entry(entries_farme,textvariable=job ,width=20,font=(16))
txjob.place(x=120,y=90)

lblGender = Label(entries_farme,text="Gender",font=(16),bg="#2c3e50",fg="white")
lblGender.place(x=10,y=130)
comboGender = ttk.Combobox(entries_farme,textvariable = gender,state="readonly",width=18,font=(16))
comboGender["values"] = ("Male","Female")
comboGender.place(x=120,y=130)

lblAge = Label(entries_farme,text="Age",font=(16),bg="#2c3e50",fg="white")
lblAge.place(x=10,y=170)
txAge = Entry(entries_farme,textvariable = age,width=20,font=(16))
txAge.place(x=120,y=170)

lblEmail = Label(entries_farme,text="Email",font=(16),bg="#2c3e50",fg="white")
lblEmail.place(x=10,y=210)
txEmail = Entry(entries_farme,textvariable = email,width=20,font=(16))
txEmail.place(x=120,y=210)

lblmobile = Label(entries_farme,text="Mobile",font=(16),bg="#2c3e50",fg="white")
lblmobile.place(x=10,y=250)
txmobile = Entry(entries_farme,textvariable = mobile,width=20,font=(16))
txmobile.place(x=120,y=250)

lblAddress = Label(entries_farme,text="Address :",font=(16),bg="#2c3e50",fg="white")
lblAddress.place(x=10,y=290)
txtAddress = Text(entries_farme,width=30,height=2,font=(16))
txtAddress.place(x=10,y=330)

#====== Define========

def hide():
    root.geometry("360x515")
    root.resizable(True,True)
def show():
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    root.geometry("%dx%d" % (width, height))
    root.resizable(True, True)
btnhide = Button(entries_farme,text="HIDE",command=hide)
btnhide.place(x=270,y=10)

btnshow = Button(entries_farme,text="SHOW",command=show)
btnshow.place(x=310,y=10)

def getDate(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[6])
    mobile.set(row[5])
    txtAddress.delete("1.0",END)
    txtAddress.insert(END,row[7])
def delete():
    data_sql.remove(row[0])
    Clear()
    displayAll()


def displayAll():
    tv.delete(*tv.get_children())
    for row in data_sql.fetch():
        tv.insert("",END,values=row)



def Clear():

    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    email.set("")
    mobile.set("")
    txtAddress.delete(1.0, END)


def add_employee():
    if txName.get() == "" or txAge.get() == "" or txjob.get() == "" or txEmail.get() == "" or txmobile.get() == "" or comboGender.get() == "" or txtAddress.get(1.0,END) == "":
        messagebox.showerror("Error","Pleas Fill all the Entry")
        return
    data_sql.insert(
        txName.get(),
        txAge.get(),
        txjob.get(),
        txEmail.get(),
        txmobile.get(),
        comboGender.get(),
        txtAddress.get(1.0,END))

    Clear()
    displayAll()

def update():
    if txName.get() == "" or txAge.get() == "" or txjob.get() == "" or txEmail.get() == "" or txmobile.get() == "" or comboGender.get() == "" or txtAddress.get(1.0,END) == "":
        messagebox.showerror("Error","Pleas Fill all the Entry")
        return
    data_sql.update(row[0],
        txName.get(),
        txAge.get(),
        txjob.get(),
        txEmail.get(),
        txmobile.get(),
        comboGender.get(),
        txtAddress.get(1.0, END))

    Clear()
    displayAll()




#====== Buttons Frame======

btn_frame = Frame(entries_farme,bg="white",bd=1,relief=SOLID)
btn_frame.place(x=10,y=400,width=340,height=100)

btnAdd = Button(btn_frame,text="Add Details",width=14,height=1,font=(16),fg="white",bg="#16a085",command=add_employee)
btnAdd.place(x=4,y=5)

btnEdit = Button(btn_frame,text="Update",width=14,height=1,font=(16),fg="white",bg="#16a085",command=update)
btnEdit.place(x=4,y=50)

btnDelete = Button(btn_frame,text="Delete",width=14,height=1,font=(16),fg="white",bg="#16a085",command=delete)
btnDelete.place(x=170,y=5)

btnClear = Button(btn_frame,text="Clear",width=14,height=1,font=(16),fg="white",bg="#16a085",command=Clear)
btnClear.place(x=170,y=50)

#========= Table Frame =====

tree_Frame = Frame(root,bg="white")
tree_Frame.place(x=365,y=1,width=1160,height=830)

style= ttk.Style()

style.configure("mystyle.Treeview",font=13,rowheight=50)
style.configure("mystyle.Treeview.Heading",fond=(13))
tv = ttk.Treeview(tree_Frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width="15")
tv.heading("2",text="Name")
tv.column("2",width="80")
tv.heading("3",text="Age")
tv.column("3",width="15")
tv.heading("4",text="Job")
tv.column("4",width="90")
tv.heading("5",text="Email")
tv.column("5",width="170")
tv.heading("7",text="Gender")
tv.column("7",width="80")
tv.heading("6",text="Mobile")
tv.column("6",width="150")
tv.heading("8",text="Address")
tv.column("8",width="190")



tv["show"] = "headings"



tv.place(x=1,y=1,height=830,width=1160)
tv.bind("<ButtonRelease-1>",getDate)

displayAll()

root.mainloop()
