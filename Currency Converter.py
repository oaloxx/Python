from tkinter import *
import tkinter as tk
import requests
from tkinter import ttk
from tkinter import messagebox

def convert_currency():
    amount = amounta.get()
    from_currency = currency_1a.get()
    to_currency = currency_2a.get()
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    exchange_rates = response.json()["rates"]
    if to_currency in exchange_rates:
        converted_amount = float(amount) * exchange_rates[to_currency]

        textbox.insert(END,f"{amount} {from_currency} = {converted_amount} {to_currency}\n")

    else:
        messagebox.showerror("Error","Please check the currency symbol if it is valid or the value of the money")

def now():
    currency_1a.set("")
    amounta.set("")
    currency_2a.set("")


def clal():
    now()
    textbox.delete("1.0", "end")

window=tk.Tk()
window.geometry("600x400")
window.title("Currency Converter")

currency_1 = Label(window,text="Currency",font=(NORMAL,20))
currency_1.place(x=5,y=5)

currency_1a = ttk.Combobox(window, width=20,font=(NORMAL,20))
currency_1a["values"] = ("ERU","USD","AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN"
                         ,"BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN"
                         ,"BWP","BYR","BZD","CAD","CDF","CHF","CKD","CLP","CNY","COP","CRC","CUP"
                         ,"CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","FJD","FKP","FOK"
                         ,"GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HNL"
                         ,"HTG","HUF","IDR","ILS","IMP","JPY","KES","KGS","KHR","KPW","KRW","KWD"
                         ,"LBP","LKR","LRD","LYD","MDL","MOP","MWK","MXN","NGN","NPR","OMR","PAB"
                         ,"PHP","PKR","PLN","QAR","RON","RSD","RUB","SAR","SBD","SDG","SEK","SLL"
                         ,"SOS","SYP","THB","TRY","TWD","UAH","VND","VUV","WST","XAF","XCD","XOF"
                         ,"XPF","YER","ZMW","ZWL")
currency_1a.place(x=250,y=5)


amount = Label(window,text="Amount",font=(NORMAL,20))
amount.place(x=5,y=50)

amounta = ttk.Combobox(window, width=20,font=(NORMAL,20))
amounta["values"] = ("50","100","200","250","500","1000","2500","5000","10000","15000","20000","50000","75000","100000")
amounta.place(x=250,y=50)

to_currency = Label(window,text="Currency to ",font=(NORMAL,20))
to_currency.place(x=5,y=100)

currency_2a = ttk.Combobox(window, width=20,font=(NORMAL,20))
currency_2a["values"] = ("ERU","USD","AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN"
                         ,"BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN"
                         ,"BWP","BYR","BZD","CAD","CDF","CHF","CKD","CLP","CNY","COP","CRC","CUP"
                         ,"CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","FJD","FKP","FOK"
                         ,"GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HNL"
                         ,"HTG","HUF","IDR","ILS","IMP","JPY","KES","KGS","KHR","KPW","KRW","KWD"
                         ,"LBP","LKR","LRD","LYD","MDL","MOP","MWK","MXN","NGN","NPR","OMR","PAB"
                         ,"PHP","PKR","PLN","QAR","RON","RSD","RUB","SAR","SBD","SDG","SEK","SLL"
                         ,"SOS","SYP","THB","TRY","TWD","UAH","VND","VUV","WST","XAF","XCD","XOF"
                         ,"XPF","YER","ZMW","ZWL")
currency_2a.place(x=250,y=100)

convert = Button(window,text="Convert",font=(NORMAL,30),width=10,bg="#76D7C4",command=convert_currency)
convert.place(x=5,y=150)

Now = Button(window,text="Now",font=(NORMAL,30),width=4,bg="#76D7C4",command=now)
Now.place(x=250,y=150)

Clear = Button(window,text="Clear all",font=(NORMAL,30),width=9,bg="#76D7C4",command=clal)
Clear.place(x=360,y=150)

textbox = Text(window)
textbox.place(x=5, y=240, width=580, height=150)



window.mainloop()

