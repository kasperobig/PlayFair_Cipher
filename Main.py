from tkinter import*
from tkinter import ttk
from Playfair import encode
from Playfair import decode

het = 400
wih = 600


def Encall(mes, key):
    text = encode(mes, key)
    lab['text'] = 'Encrypted Cipher text: '+text


def Dcrcall(mes, key):
    text = decode(mes, key)
    lab['text'] = 'Decrypted Message: '+text


root = Tk()
