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
        self.input1 = Text(self)
        self.input1.config(width=30, height=15)
        self.input1.insert('0.0', 'Oh it is scary')
        self.input1.place(x=50, y=30)
        self.input2 = Text(self)
        self.input2.config(width=30, height=15)
        self.input2.insert('0.0', 'derknabeimmoor')
        self.input2.place(x=320, y=30)
        self.bStart = Button(self, text="Encrypt/Decrypt")
        self.bStart.bind("<Button-1>", self.starten)
        self.bStart.place(x=220, y=235)
        self.label = Label(self, text="Encrypted Text")
        self.label.config(bg="lightgray")
        self.label.place(x=550, y=10)
        self.inputText = Text(self)
        self.inputText.config(width=30, height=15)
        self.inputText.place(x=550, y=30)

    def start(self, event):
        self.playfair = Playfair(self.input1.get(
            "1.0", "1.end"), self.input2.get("1.0", "1.end"))
        self.playfair.textFormation()
        self.playfair.Alphabet()
        print(self.playfair.code())
        #textneu = self.playfair.globall
        #self.label.config(text = self.playfair.globall)
        self.inputText.insert(END, self.playfair.globall)
