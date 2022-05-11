from appJar import gui
from Playfair import *

app = gui()

# Create label
app.addLabel("Playfair", "Playfair Encryption")


def press(button):
    if button == "Cancel":
        app.stop()
