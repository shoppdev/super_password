# gui giving option to create a password, check a password or update an existing password(leet it)
# import tkinter
from tkinter import *

from tkinter.ttk import *  # gives a modern look to the gui
import pass_creator

''' four buttons on open (password gen, password check, password change, close '''


def get_pw():
    #label = Label(text=f'random pw- {pass_creator.make_password(12)}').pack()
    box = Text(height=1, width=52)
    box.insert(INSERT, pass_creator.make_password(12))
    box.pack()
    value = box.get('1.0', 'end-1c')
    print(value)

def gen_password():
    gen = Tk()
    gen.title('Generate Password')
    gen.geometry('270x150')
    button = Button(gen, text='Generate')
    close = Button(gen, text='Close', command=gen.destroy)

    button.pack()
    close.pack()




def start_gui():
    gui = Tk()
    gui.title('Super Password!')
    gui.geometry('270x150')

    gen_pass = Button(gui, text='Gen. Pass', command=gen_password)
    check_pass = Button(gui, text='Check Pass')
    leet_pass = Button(gui, text='Leet Pass')
    close_btn = Button(gui, text='Close', command=gui.destroy)

    # w = Text(gui)
    # w.insert(INSERT, 'Ho ho')
    # w.pack()
    gen_pass.pack()
    check_pass.pack()
    leet_pass.pack()
    close_btn.pack()



    gui.mainloop()

start_gui()
