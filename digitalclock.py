from tkinter import *
from tkinter import ttk
from tkinter import font
#import time
import datetime


def quit_(*args):
    root.destroy()


def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%d-%m-%Y  %H:%M:%S"))

    txt.set(time)
    root.after(1, clock_time)


root = Tk()
root.geometry("800x200")
root.attributes("-fullscreen", False)
root.configure(background='White')
root.bind("x", quit_)
root.after(1, clock_time)
txt = StringVar()
fnt = font.Font(family='Times New Roman', size=60, weight='bold')
#txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="black", background="white")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
