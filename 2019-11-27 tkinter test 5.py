#Dominik Zimny
#27/11/2019
from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = Label(window, text = "Hello")

lbl.grid(column = 0, row = 0)

btn = Button(window, text = "Click Me")

btn.grid(column = 1, row = 0)

window.mainloop()
