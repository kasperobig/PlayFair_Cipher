import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *

# Creating a window
root = tk.Tk()

# For changing the icon of the title bar
pic = PhotoImage(file="png-tra.png")
root.iconphoto(False, pic)
# For changing the title of the title bar
root.title("Playfair Encryptor-Decryptor")

# To set the dimensions of the window
root.geometry("400x500")  # width x height
# To set whether we can resize the window or not.The below line doesn't allow the resizing of the window.
root.resizable(width=FALSE, height=FALSE)

# Creating a canvas
canvas = tk.Canvas(root, height=500, width=400, bg="MediumPurple1")
# Attaching the canvas
canvas.pack()

root.mainloop()
