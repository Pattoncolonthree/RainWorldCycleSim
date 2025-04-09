import tkinter as tk
from tkinter import *
import time
import os
from PIL import Image, ImageTk
from itertools import count



class App(tk.Tk):
   def __init__(self):
      super().__init__()
app = App()



app.geometry("900x700")
app.title("Cycle sim")
app.configure(background='#eeefff')



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
            self.delay = 100

        if len(self.frames) == 100:
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



def printString(string):
    for char in string:
        Label.configure(text=Label.cget('text') + char, font=('Arial', 18),fg="#b00b1e")
        Label.update()
        time.sleep(.05)
    time.sleep(5)
    text = " "


text = " hiii"

Label = tk.Label(app)



slug = ImageLabel(app)
Label.pack(padx=10, pady=10)
Label.place(x= 0, y= 575)
slug.pack(padx=10, pady=10)
slug.load('scavandscug.gif')
slug.place(x= 0, y=0)
time.sleep(1)
printString(text)
time.sleep(2)
text = " hiii"
printString(text)


#scav = ImageLabel(app)
#scav.pack(padx=10, pady=10)
#scav.load('scav.gif')
#scav.place(x= 650, y=50)

app.mainloop()