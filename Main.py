from cProfile import label
from logging import root
from tkinter import *
from turtle import right

# Crate new window
windows = Tk()

windows.title("PlayFair")
windows.geometry("400x500")
windows.iconbitmap("logo.ico")
windows.config(background='#41B77F')

global entry1
global entry2


Label(windows, text="Plaintext").place(20, 20)
Label(windows, text="key").place(20, 20)

entry1 = Entry(windows, bd=5)
entry1.place(140, 70)

entry2 = Entry(windows, bd=5)
entry2.place(140, 70)


windows.mainloop()
