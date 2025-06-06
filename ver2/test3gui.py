
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



class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 1000

        if len(self.frames) == 1000:
            self.config(image=self.frames[0])
        else:
            self.next_frame()



    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

length = "wwwwwwwwwwwwwwwwwwwww"

#wwwwwwwwwwwwwwwwwwwww
def sleepy():
    for char in length:
        time.sleep(0.05)
        Label.update()


def printString(string):
    for char in string:
        Label.configure(text=Label.cget('text') + char, font=('Arial', 18, 'bold'), fg="#d1cdf0", bg="#180821")
        Label.update()
        time.sleep(0.0625)
    sleepy()
    text = Label.configure(text= " ")
    Label.update

   


Label = tk.Label(app)
Label.pack(padx=10, pady=10)
Label.place(x= 110, y= 575)

ImageLabel(bg="#180821")
slug = ImageLabel(app, borderwidth = 0)
slug.pack(padx=10, pady=10)
slug.load('scavandscug.gif')
slug.place(x= 0, y=0)


#button1Clicked  = False
#button2Clicked  = False

#def option1(buttonClicked):
#  print( "")
#  print(buttonClicked)
#  buttonClicked = not buttonClicked 
#  button1["state"] = DISABLED
#  button2["state"] = DISABLED
    
#def option2():
#  global button2Clicked
#  button2Clicked = not button2Clicked 
#  button2["state"] = DISABLED
#  button1["state"] = DISABLED


#button1 = tk.Button(app, 
#                   text="", 
#                   command=option1(button1Clicked),
#                   activebackground="#49365a", 
#                   activeforeground="#d1cdf0",
#                   bd=0,
#                   bg="#332441",
#                   cursor="hand2",
#                   disabledforeground="#484659",
#                   fg="#d1cdf0",
#                   font=("Arial", 12, 'bold'),
#                   height=2,
#                   highlightbackground="black",
#                   highlightcolor="green",
#                   padx=10,
#                   pady=5,
#                   width=15)
#button1.pack(padx=20, pady=20)
#button1.place(x=200, y=635)


#button2 = tk.Button(app, 
#                   text="", 
#                   command=option1(button2Clicked),
#                   activebackground="#49365a", 
#                   activeforeground="#d1cdf0",
#                   bd=0,
#                   bg="#332441",
#                   cursor="hand2",
#                   disabledforeground="#484659",
#                   fg="#d1cdf0",
#                   font=("Arial", 12, 'bold'),
#                   height=2,
#                   highlightbackground="black",
#                   highlightcolor="green",
#                   padx=10,
#                   pady=5,
#                   width=15)
#button2.pack(padx=20, pady=20)
#button2.place(x=600, y=635)


