from tkinter import *
import math
import sys
import time
import sched

root = Tk()
app = Frame(root)
app.grid()

root.resizable(0,0)
root.title("Game")

#Variable
clickcount = IntVar()
clickcount.set(0)

#Timer
starttime = 0
currenttime = 0
timeron = IntVar()
timeron.set(0)

#Define
def count():   
    global starttime, currenttime, timeron, clickcount
    clickcount.set(clickcount.get() + 1)
    if not starttime:
        starttime = time.time() - 1
    if timeron.get() >= 10:
        button.config(state=DISABLED)
        b.config(state=DISABLED)
    currenttime = time.time()
    timeron.set(int(currenttime - starttime))


def game():
    global button
    global text
    global timer
    text = Label(app, text="You have ten seconds. Start clicking :)")
    button = Button(app, text="Click here", textvariable=clickcount, command=count)
    timer = Label(app, text="Time", textvariable=timeron)

    text.grid(row=3, column=1, columnspan=4)
    button.grid(row=4, column=2, columnspan=2, sticky="ew")
    timer.grid(row=5, column=2, sticky="ew")

def reset():
    button.config(state=NORMAL)
    b.config(state=NORMAL)
    global starttime, currenttime, timeron, clickcount
    if timeron.get() >=10:
        starttime = 0
        currenttime = 0
        timeron.set(0)
        clickcount.set(0)

def quit(root):
    root.destroy()


def about():
    master = Tk()
    master.title("About")

    w = Label(master, text="Created By Zac Hadjineophytou")
    w.pack()

    master.mainloop()

#Menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Reset", command=reset)
filemenu.add_command(label="Quit", command=lambda root=root:quit(root))

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about)


#Start Instructions
global b
w = Label(app, text="You have ten seconds to click the button as many times as possible")
b = Button(app, text="Start", command=game)

w.grid(row=1, column=1, columnspan=4)
b.grid(row=2, column=2, columnspan=2, sticky="ew")

#End program

root.mainloop()
