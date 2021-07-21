# gui giving option to create a password, check a password or update an existing password(leet it)
# import tkinter
from tkinter import *

from tkinter.ttk import *  # gives a modern look to the gui
import pass_creator
import pwnd_check

''' four buttons on open (password gen, password check, password change, close '''


def get_pw(window):

    box = Text(window, height=1, width=52)
    box.insert(INSERT, pass_creator.make_password(12))
    box.pack()


def gen_password():
    gen = Tk()
    gen.title('Generate Password')
    gen.geometry('270x150')
    button = Button(gen, text='Generate', command=lambda: get_pw(gen))
    close = Button(gen, text='Close', command=gen.destroy)

    button.pack()
    close.pack()


def display_text():
    pass


def check_password():
    pwn = Tk()
    pwn.title('PWND Check')
    pwn.geometry('270x150')
    check = Button(pwn, text='Check')
    close = Button(pwn, text='Close', command=pwn.destroy)

    check.pack()
    close.pack()


def start_gui():
    gui = Tk()
    gui.title('Super Password!')
    gui.geometry('270x150')

    gen_pass = Button(gui, text='Gen. Pass', command=gen_password)
    check_pass = Button(gui, text='Check Pass', command=check_password)
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
