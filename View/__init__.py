from tkinter import *
from tkinter import ttk
import datetime

class Start:

    def __init__(self,root):

        def exit_full_screen(event):
            root.overrideredirect(False)

        root.bind("<Escape>", exit_full_screen)
        root.configure(background="black")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w, h))

        root.overrideredirect(True)


        time = time_panel(root)


def time_panel(root):

    t = StringVar()

    time = Label(root, textvariable=t, font=("Helvetica", 80), fg="white", bg="Black")
    time.place(relx=0.85, rely=0.1, anchor=CENTER)

    now = datetime.datetime.now()
    t.set(now.time())

    #time.after(2, time_panel(root))
#
    #return time

def tick(time):
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    time.config(text=time2)
    time.after(500, tick(time))


root = Tk()

app = Start(root)

root.mainloop()
