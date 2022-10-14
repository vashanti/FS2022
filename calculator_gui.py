from tkinter import *

def addNumbers():
    res = int(entry1.get()) + int(entry2.get())
    resultsVar.set(res)
    print(res)

def subNumbers():
    res = int(entry1.get()) - int(entry2.get())
    resultsVar.set(res)
    print(res)

def mulNumbers():
    res = int(entry1.get()) * int(entry2.get())
    resultsVar.set(res)
    print(res)

def divNumbers():
    res = int(entry1.get()) / int(entry2.get())
    resultsVar.set(res)
    print(res)

master = Tk()
resultsVar = StringVar()
master.geometry("500x600")
master.title("My Calculator")

Label(master, text="My Awesome Calculator").grid(row=1, column=4)

Label(master, text="First Number").grid(row=2, column=1)
Label(master, text="Second Number").grid(row=3, column=1)
results = Label(master, text="", textvariable=resultsVar).grid(row=3, column=3)

entry1 = Entry(master)
entry2 = Entry(master)

entry1.grid(row=2,column=2)
entry2.grid(row=3,column=2)

Button(master,text="+", command=addNumbers).grid(row=4, column=1)
Button(master,text="-", command=subNumbers).grid(row=4, column=2)
Button(master,text="*", command=mulNumbers).grid(row=4, column=3)
Button(master,text="/", command=divNumbers).grid(row=4, column=4)
master.mainloop()