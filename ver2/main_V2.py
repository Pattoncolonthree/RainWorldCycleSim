
import tkinter as tk
from tkinter import *
import time
import os
from PIL import Image, ImageTk
from itertools import count
import winsound

class App(tk.Tk):
   def __init__(self):
      super().__init__()
app = App()

app.geometry("1006x700")
app.title("Cycle sim")
app.configure(background='#180821')

button1Clicked  = False
button2Clicked  = False
def buttonpressed1():
  button1Clicked = True


def option1():
  buttonpressed1()
  button1["state"] = DISABLED
  button2["state"] = DISABLED
    
def option2():
  button2Clicked = True
  button2["state"] = DISABLED
  button1["state"] = DISABLED


button1 = tk.Button(app, 
                   text="woah", 
                   command=option1,
                   activebackground="#49365a", 
                   activeforeground="#d1cdf0",
                   bd=0,
                   bg="#332441",
                   cursor="hand2",
                   disabledforeground="#484659",
                   fg="#d1cdf0",
                   font=("Arial", 12, 'bold'),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   padx=10,
                   pady=5,
                   width=15)
button1.pack(padx=20, pady=20)
button1.place(x=200, y=635)


button2 = tk.Button(app, 
                   text="whatt", 
                   command=option2,
                   activebackground="#49365a", 
                   activeforeground="#d1cdf0",
                   bd=0,
                   bg="#332441",
                   cursor="hand2",
                   disabledforeground="#484659",
                   fg="#d1cdf0",
                   font=("Arial", 12, 'bold'),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   padx=10,
                   pady=5,
                   width=15)
button2.pack(padx=20, pady=20)
button2.place(x=600, y=635)


if button1Clicked == True:
  print("yay")


if button2Clicked:
  print("ywwoah")


mainloop()