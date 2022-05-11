from tkinter import *
from Playfair import *


class PlayfairInter(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Playfair")
        self.place(x=0, y=0)
        self.config(width=900, height=330)
        self.createWidgets()

    def createWidgets(self):
        self.clearword = Label(
            self, text="Please Enter The word to be crypted: ")
        self.clearword.place(x=50, y=10)
        self.clearword = Label(self, text="Enter key: ")
        self.clearword.place(x=320, y=10)
        self.eingabe1 = Text(self)
        self.eingabe1.config(width=30, height=15)
        self.eingabe1.insert('0.0', 'Oh it is scary')
        self.eingabe1.place(x=50, y=30)
        self.eingabe2 = Text(self)
        self.eingabe2.config(width=30, height=15)
        self.eingabe2.insert('0.0', 'derknabeimmoor')
        self.eingabe2.place(x=320, y=30)
