from tkinter import *
from Playfair import *


class PlayfairInter(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Playfair")
        self.place(x=0, y=0)
        self.config(width=900, height=330)
        self.createWidgets()
