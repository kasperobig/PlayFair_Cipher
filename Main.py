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
canvas = tk.Canvas(root, height=500, width=400, bg="#2196F3")
# Attaching the canvas
canvas.pack()

# Set the family,size and style of the font
bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

# Creating a label with a key and attaching it to the root
label1 = tk.Label(root, text="Enter the Key", width=20, bg="#2196F3")
# adding the font features to the label
label1.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(200, 100, window=label1)

# Text Area
user_text = tk.Entry(root)
canvas.create_window(200, 150, window=user_text)

root.mainloop()
