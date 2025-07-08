
import tkinter as tk
from tkinter import *
import time
import os
from PIL import Image, ImageTk
from itertools import count
import winsound
import GUI_Creature_Interactions as ci
import Starting_Room as R1

class App(tk.Tk):
   def __init__(self):
      super().__init__()
app = App()


R1.room1()

ci.Scavgui()

app.mainloop()