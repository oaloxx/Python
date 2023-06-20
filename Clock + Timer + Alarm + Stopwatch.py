import tkinter as tk 
from tkinter import ttk  
from time import strftime
from tkinter import *
import time
import winsound
from tkinter import messagebox

root = tk.Tk()
root.title('Clock')
root.resizable(False,False)
root.geometry("600x250")

time_var = tk.StringVar()
time_var.set(time.strftime('%H:%M:%S'))
time_label = tk.Label(root, textvariable=time_var, font=('Helvetica', 48))
time_label.place(y=0,x=330)

timer_running = False
timer_count = 0
timer_var = tk.StringVar()
timer_var.set('00:00:00')


alarm_running = False
alarm_time = None
alarm_var = tk.StringVar()
alarm_var.set('Set alarm')
alarm_label = tk.Label(root, textvariable=alarm_var, font=('Helvetica', 24))
alarm_label.pack()

stopwatch_running = False
stopwatch_count = 0
stopwatch_var = tk.StringVar()
stopwatch_var.set('00:00:00')
stopwatch_label = tk.Label(root, textvariable=stopwatch_var, font=('Helvetica', 24))
stopwatch_label.pack()

def update_clock():
    global timer_running, alarm_running, stopwatch_running
    global timer_count, alarm_time, stopwatch_count

    time_var.set(time.strftime('%H:%M:%S'))
    root.after(1000, update_clock)

    if alarm_running and time.time() >= alarm_time:
        alarm_var.set('Alarm!')
        alarm_running = False

    if timer_running:
        timer_count -= 1
        if timer_count <= 0:
            timer_var.set('00:00:00')
            timer_running = False
        else:
            minutes, seconds = divmod(timer_count, 60)
            hours, minutes = divmod(minutes, 60)
            timer_var.set('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

    if stopwatch_running:
        stopwatch_count += 1
        minutes, seconds = divmod(stopwatch_count, 60)
        hours, minutes = divmod(minutes, 60)
        stopwatch_var.set('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

def toggle_timer():
    global timer_running, timer_count,f1
    f1 = Frame(width=430,height=250,bg="black")
    f1.place(x=175,y=0)

    saxa1 = ttk.Combobox(f1, state="readonly",width=3)
    saxa1["values"] = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24')
    saxa1.place(x=1, y=1)


    mint1 = ttk.Combobox(f1, state="readonly", width=3)
    mint1["values"] = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
    mint1.place(x=50, y=1)

    sik1 = ttk.Combobox(f1, state="readonly", width=3)
    sik1["values"] = ('00', '01', '02', '03', '04', '05', '06', '07',
                      '08', '09', '10', '11', '12', '13', '14', '15',
                      '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '31',
                      '32', '33', '34', '35', '36', '37', '38', '39',
                      '40', '41', '42', '43', '44', '45', '46', '47',
                      '48', '49', '50', '51', '52', '53', '54', '55',
                      '56', '57', '58', '59', '60')
    sik1.place(x=100, y=1)




    timer_label = tk.Label(f1,textvariable=timer_var,bg="black",fg="white", font=('Helvetica', 74))
    timer_label.place(y=70, x=15)


    if not timer_running:
        def true():
            global timer_running, timer_count
            timer_running = not timer_running

            if timer_running:
                hours = int(saxa1.get())
                minutes = int(mint1.get())
                seconds = int(sik1.get())
                timer_count = hours * 3600 + minutes * 60 + seconds

            else:
                timer_count = 0
                timer_var.set('00:00:00')

        Button(f1,text="Set timer",command=true,width=37).place(x=150,y=1)



def set_alarm():
    f4 = Frame(root, width=430, height=250, bg="black")
    f4.place(x=175, y=0)

    global saxa
    saxa = ttk.Combobox(f4, state="readonly", width=3)
    saxa["values"] = ('00', '01', '02', '03', '04', '05', '06', '07',
                      '08', '09', '10', '11', '12', '13', '14', '15',
                      '16', '17', '18', '19', '20', '21', '22', '23', '24')
    saxa.place(x=1, y=3)

    global mint
    mint = ttk.Combobox(f4, state="readonly", width=3)
    mint["values"] = ('00', '01', '02', '03', '04', '05', '06', '07',
                      '08', '09', '10', '11', '12', '13', '14', '15',
                      '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '31',
                      '32', '33', '34', '35', '36', '37', '38', '39',
                      '40', '41', '42', '43', '44', '45', '46', '47',
                      '48', '49', '50', '51', '52', '53', '54', '55',
                      '56', '57', '58', '59', '60')
    mint.place(x=50, y=3)



    global sik
    sik = ttk.Combobox(f4, state="readonly", width=3)
    sik["values"] = ('00', '01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12', '13', '14', '15',
                     '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '31',
                     '32', '33', '34', '35', '36', '37', '38', '39',
                     '40', '41', '42', '43', '44', '45', '46', '47',
                     '48', '49', '50', '51', '52', '53', '54', '55',
                     '56', '57', '58', '59', '60')
    sik.place(x=100, y=3)

    from datetime import datetime

    def print_time():

        current_time = datetime.now().strftime('%H:%M:%S')
        time_label.config(text=current_time)
        time_label.after(1000, print_time)


        if current_time == f"{saxa.get()}:{mint.get()}:{sik.get()}":
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)




    time_label = tk.Label(f4, font=('calibri', 40, 'bold'), background='black', foreground='white')
    time_label.place(x=190,y=20)

    print_time()

    def prin():

        current_time1 = int(datetime.now().strftime('%H'))
        current_time2 = int(datetime.now().strftime('%M'))

        x1 = int(24 - current_time1)
        x2 = int(60 - current_time2)


        messagebox.showinfo("Alarm",f"The alarm is set to {saxa.get()} and {mint.get()} min ")


    Button(f4, text="Set alarm",width=37,command=prin).place(x=150,y=1)



f3 = tk.Frame(width=430, height=250, bg="black")
f3.place(x=175, y=0)

start_time = 0.0
running = False
elapsed_time = 0.0

def stop_watch():


    global time_label, start_button, stop_button, reset_button
    f3.lift()
    f3.place(x=175, y=0,width=430, height=250)

    time_label = tk.Label(f3, text="00:00:00.0", font=("Helvetica", 60),fg="white",bg="black")
    start_button = tk.Button(f3, font=(5),text="Start", command=start,bg="#424949",fg="white")
    stop_button = tk.Button(f3,font=(5),text="Stop", command=stop,bg="#424949",fg="white")
    reset_button = tk.Button(f3,font=(5),text="Reset", command=reset, state="disabled",bg="#424949",fg="white")
    time_label.place(x=25,y=50)
    start_button.place(x=0,y=200,width=150,height=50)
    stop_button.place(x=140,y=200,width=150,height=50)
    reset_button.place(x=290,y=200,width=150,height=50)

def start():
    global start_time, running
    if not running:
        start_time = time.monotonic()
        update()
        running = True
        reset_button.config(state="disabled")

def stop():
    global running, elapsed_time
    if running:
        f3.after_cancel(after_id)
        elapsed_time += time.monotonic() - start_time
        running = False
        reset_button.config(state="normal")

def reset():
    global elapsed_time, running
    elapsed_time = 0.0
    running = False
    time_label.config(text="00:00:00.0")
    reset_button.config(state="disabled")

def update():
    global after_id
    delta_time = time.monotonic() - start_time + elapsed_time
    minutes, seconds = divmod(delta_time, 60)
    hours, minutes = divmod(minutes, 60)
    time_label.config(text="{:02.0f}:{:02.0f}:{:04.1f}".format(hours, minutes, seconds))
    after_id = f3.after(10, update)




def normal_uhr():
    f2 = Frame(root,width=430, height=250, bg="black")
    f2.place(x=175, y=0)


    def my_time():
        time_string = strftime('%H:%M:%S %p')
        l1.config(text=time_string)
        l1.after(1000, my_time)

    l1 = tk.Label(f2,fg="white",bg="black",font=('Helvetica', 74))
    l1.place(y=70, x=15)

    my_time()



button1 = tk.Button(root, text='Clock',font=(6),width=15,height=2,command=normal_uhr)
button1.place(x=0,y=0)
button1.invoke()

timer_button = tk.Button(root, text='Timer',font=(6),width=15,height=2, command=toggle_timer)
timer_button.place(x=0,y=62)

alarm_button = tk.Button(root, text='Alarm',font=(6),width=15,height=2, command=set_alarm)
alarm_button.place(x=0,y=124)

stopwatch_button = tk.Button(root, text='Stopwatch',font=(6),width=15,height=2,command=stop_watch)
stopwatch_button.place(x=0,y=186)

update_clock()
root.mainloop()
