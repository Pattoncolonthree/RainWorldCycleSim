import tkinter as tk
from tkinter import *
import time
import os
from PIL import Image, ImageTk
from itertools import count
import winsound
from Creatureinteractions import *
class App(tk.Tk):
   def __init__(self):
      super().__init__()
app = App()



app.geometry("1006x700")
app.title("Cycle sim")
app.configure(background='#93a0bb')



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
slength = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
spritelength = "wwwwwwwwwwwwwwwwwwwwwwww"
def sleepy():
    for char in length:
        time.sleep(0.05)
        Label.update()


def wait():
    for char in spritelength:
        time.sleep(0.0625)
        Label.update()

def stringlength():
    for char in slength:
        time.sleep(0.0625)
        Label.update()

def printString(string):
    for char in string:
        Label.configure(text=Label.cget('text') + char, font=('Arial', 18, 'bold'), fg="#2b213e", bg="#93a0bb")
        Label.update()
        time.sleep(0.0625)
    sleepy()
    text = Label.configure(text= " ")
    Label.update

def longprintString(string):
    for char in string:
        Label.configure(text=Label.cget('text') + char, font=('Arial', 18, 'bold'), fg="#2b213e", bg="#93a0bb")
        Label.update()
        stringlength()
    sleepy()
    text = Label.configure(text= " ")
    Label.update


   


Label = tk.Label(app)
Label.pack(padx=10, pady=10)
Label.place(x= 110, y= 575)

ImageLabel(bg="#93a0bb")
slug = ImageLabel(app, borderwidth = 0)
slug.pack(padx=10, pady=10)
slug.load('scavandscug.gif')
slug.place(x= 0, y=0)

