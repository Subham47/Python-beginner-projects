from tkinter import *
from tkinter import ttk
from tkinter import font
import datetime

def quit_(*args):
    root.destroy()

def clock_count():
    lefttime = endtime - datetime.datetime.now()
    lefttime = lefttime - datetime.timedelta(microseconds = lefttime.microseconds)
    if lefttime.seconds<=0:
        quit_()
    txt.set(lefttime)
    root.after(1, clock_count)
    #print(lefttime)



root = Tk()
root.geometry("600x200")
root.attributes("-fullscreen", True)
root.configure(background='green')
root.bind("x", quit_)
root.after(1, clock_count)
txt = StringVar()
endtime = datetime.datetime(2021, 6, 2, 15, 0, 0)
fnt = font.Font(family='Helvetica', size=120, weight='bold')
#txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="green")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
exit_button = Button(root, text="Exit", command=quit_)
exit_button.pack(pady=100)

root.mainloop()
