from tkinter import *

master = Tk()
master.geometry("500x600")
master.title("My Calculator")

Label(master, text="My Awesome Calculator").grid(row=1, column=4)

Label(master, text="First Number").grid(row=2, column=1)
Label(master, text="Second Number").grid(row=3, column=1)

Entry(master).grid(row=2,column=2)
Entry(master).grid(row=3,column=2)

Button(master,text="+").grid(row=4, column=1)
Button(master,text="-").grid(row=4, column=2)
Button(master,text="*").grid(row=4, column=3)
Button(master,text="/").grid(row=4, column=4)
master.mainloop()