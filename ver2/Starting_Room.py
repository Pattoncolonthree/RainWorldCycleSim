import time
import random
import sys
import winsound
import threading
import defs as d

class App(tk.Tk):
   def __init__(self):
      super().__init__()
app = App()

def spear_chance():
    """this code will randomise with either 1 or 2 and return the output.
    """
    return random.randint(1,2)

if spear_chance() == 1:
    has_spear = True
else:
    has_spear = False


def room1():
    """
    
    
    
    """
    if  has_spear is False:
        scugr1=d.ImageLabel(d.app, borderwidth=0)
        scugr1.pack(padx=10, pady=10)
        scugr1.load('r1.gif')
        scugr1.place(x=0, y=0)
    else:
        scugr1sp=d.ImageLabel(d.app, borderwidth=0)
        scugr1sp.pack(padx=10, pady=10)
        scugr1sp.load('r1spear.gif')
        scugr1sp.place(x=0, y=0)




app.mainloop()