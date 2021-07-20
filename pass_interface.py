# gui giving option to create a password, check a password or update an existing password(leet it)
from tkinter import *

from tkinter.ttk import *  # gives a modern look to the gui

# root = Tk()
#
# root.geometry('100x100')
#
# btn = Button(root, text='Click me!', command=root.destroy)
#
# btn.pack(side='top')
#
# root.mainloop()


def start_gui():
    gui = Tk()
    gui.title('Super Password!')
    gui.geometry('270x150')

    gui.mainloop()

start_gui()
