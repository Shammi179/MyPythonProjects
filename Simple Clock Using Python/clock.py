from tkinter import *
from tkinter import font
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string1 = "SHAMMI's Clock"
    label1.config(text=string1)
    string2 = strftime('%H:%M:%S %p')
    label2.config(text=string2)
    label2.after(1000, time)


label1 = Label(root, font=("ds-digital", 30), background = "orange", foreground= "white")
label1.pack(anchor= "center")
label2 = Label(root, font= ("ds-digital", 50), background = "white", foreground= "orange")
label2.pack(anchor= "center")

time()

mainloop()