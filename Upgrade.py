from asyncio import shield
from cProfile import label
from ctypes import alignment
import tkinter
from tkinter import *
from typing import Dict
import os

global bli 
bli = []

def start():
    var = StringVar()
    global label1
    label1 = Label(textvariable = var, height=3, fg = "red",font = ('BOLD',30))
    label1.pack(side=TOP)
    var.set("       SHOPPER       ")
    global label2
    label2 = Label(text = "Welcome To SHOPPER \n\n\n To continue, Provide your details",font=('times',20),)
    label2.pack()
    global label3
    label3 = Label(text = "Name: ",font=('times',20))
    label3.pack(side=LEFT,padx=100)
    global p 
    global name
    name = StringVar()
    p = Entry(shopper,textvariable=name)
    p.pack(side=LEFT,ipadx=25)
    global amount
    amount = IntVar(value=" ")
    global m 
    m = Entry(shopper,textvariable=amount)
    m.pack(side=RIGHT,ipadx=25,padx=100)
    global wallet_amount 
    wallet_amount = Label(text = "Wallet Total: ",font=('times',20))
    wallet_amount.pack(side=RIGHT,ipadx=5)
    global button1 
    button1 = Button(text="Submit",font=('times',23),activebackground="red",activeforeground="black",command=module1)
    button1.pack(side=BOTTOM,pady=60)

def balance():
    msg.configure(textvariable= amount,bg="black",fg="white",bd=15)
    
def list_items():
    global li
    li = {"Chair" : 500, "Bench" : 1000, "Table" : 2000, "Mouse" : 350, "LG TV" : 50000, "Acer Laptop" : 25000, "Travel Bag" : 1900, "Lan Cable" : 250, "Earphones" : 2000,
    "Ipad" : 30000, "Watch" : 5000}
    li = {k6.lower(): v for k6, v in li.items()}
    msg1.configure(text="%s"%(li),bg = "white",fg='black', width = 500)
    
def bag_list():
    msg5.configure(text = "%s"%(bli),bg='white',fg='black',width=1000)

def buy():
    var1.pack_forget()
    msg2.pack_forget()
    buttonsmall.pack_forget()
    amou = amount.get()
    fl = 1 
    if item.get() not in str(li.items()) :
        msg2.configure(text = "INCORRECT NAME ENTERED, TRY AGAIN",width=300)
        msg2.pack()
        fl = 0 
    if fl == 1:
        if amou<int(li[item.get()]):
            msg2.configure(text = "CANNOT BUY THE ITEM, YOUR WALLET AMOUNT IS LOW",width=400)
            msg2.pack()
        else:
            msg2.configure(text = "ITEM PURCHASED SUCCESFULLY",width=300)
            msg2.pack()
            bli.append(item.get())
            amou = amou - int(li[item.get()])
            amount.set(amou)
    
def purchase():
    msg2.configure(text="ENTER ITEM YOU WANT TO PURCHASE",width=500)
    msg2.pack()
    global item
    item = StringVar()
    global var1
    var1 = Entry(shopper,textvariable=item)
    var1.pack()
    global buttonsmall
    buttonsmall = Button(text="purchase",bg="black",fg="red",command =buy)
    buttonsmall.pack()
    
def module1():
    #a = wallet(name,amount)
    #print("__________________________________")
    #print("To exit press 1, to view main menu press any other key : ",end="")
    #k = input()
    label2.destroy()
    label3.destroy()
    wallet_amount.destroy()
    button1.destroy()
    p.pack_forget()
    m.pack_forget()
   
    button2 = Button(shopper,text="CLICK HERE TO VIEW YOUR BALANCE",font=('times',13),activebackground="red",activeforeground="black",command=balance) 
    button2.pack(side=TOP,pady=25)
    global msg 
    msg = Message(text = " ")
    msg.pack()
    button3 = Button(shopper,text="CLICK HERE TO VIEW ITEM LIST",font=('time',13),activebackground="red",activeforeground="black",command = list_items)
    button3.pack(side=TOP,pady=25)
    global msg1
    msg1 = Message(text = " ")
    msg1.pack()
    button4 = Button(shopper,text="CLICK HERE TO VIEW YOUR PURCHASES",font=('time',13),activebackground="red",activeforeground="black",command=bag_list)
    button4.pack(side=TOP,pady=25)
    global msg5 
    msg5 = Message(text = " ")
    msg5.pack()
    button5 = Button(shopper,text="CLICK HERE TO PURCHASE ITEMS",font=('time',13),activebackground="red",activeforeground="black",command=purchase)
    button5.pack(side=TOP,pady=25)
    global msg2
    msg2= Message(text=" ")
    msg2.pack()

shopper = tkinter.Tk()
shopper.title("Shopper")


start()
shopper.mainloop()
