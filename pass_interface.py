# gui giving option to create a password, check a password or update an existing password(leet it)
from tkinter import *

from tkinter.ttk import *  # gives a modern look to the gui
import pass_creator

# root = Tk()
#
# root.geometry('100x100')
#
# btn = Button(root, text='Click me!', command=root.destroy)
#
# btn.pack(side='top')
#
# root.mainloop()

def get_pw():
    label = Label(text=f'random pw- {pass_creator.make_password(12)}').pack()
    #label.pack()

def start_gui():
    gui = Tk()
    gui.title('Super Password!')
    gui.geometry('270x150')

    button = Button(gui, text='Gen. Pass', command=get_pw)
    #label = Label(gui, text=f'random pw- {pass_creator.make_password(12)}')
    button.pack()
    #label.pack()


    gui.mainloop()

start_gui()
