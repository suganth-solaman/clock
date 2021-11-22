from tkinter import*
from tkinter.ttk import *

from time import strftime

r=Tk()
r.title("clock")
def time():
    string=strftime("%H:%M:%S %a")
    label.config(text=string)
    label.after(1000,time)

label=Label(r,font=(200),foreground="black")
label.pack(anchor="center")
time()
mainloop()