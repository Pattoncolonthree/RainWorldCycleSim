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

length = "wwwwwwwwwwwwwwwwwwww"

def sleepy():
    for char in length:
        time.sleep(0.05)
        Label.update()

def printString(string):
    for char in string:
        Label.configure(text=Label.cget('text') + char, font=('Arial', 18, 'bold'), fg="#2b213e", bg="#93a0bb")
        Label.update()
        time.sleep(.05)
    sleepy()
    text = Label.configure(text= " ")
    Label.update



   


Label = tk.Label(app)

def delete(text):
    delete = (text)

    if delete in text:
        location = text.find(delete)
        new_text = text[0:location]
        
        return printString(new_text)



ImageLabel(bg="#93a0bb")
slug = ImageLabel(app)
Label.pack(padx=10, pady=10)
Label.place(x= 110, y= 575)
LabelFrame(cnf={borderwidth = 0})
slug.pack(padx=10, pady=10)
slug.load('scavandscug.gif')
slug.place(x= 0, y=0)
time.sleep(1)

winsound.PlaySound('threat.wav', winsound.SND_ASYNC)

text = " You look towards the creature in front of you, it looks back at you\nit's quills spiking up."
printString(text)



if reputation(aggression) <= 1:
    text = ("The Scavenger looks at you warily, clutching it's spear to it's chest protectively")
    printString(text)
elif reputation(aggression) > 1 and reputation(aggression) <= 3:
    text = ("The Scavenger raises it's spear towards you, but seems more defensive than offensive")
    printString(text)
else:
    text = ("The Scavenger frills up, raising it's spear and you know it intends\n to use it.")
    printString(text)


#scav = ImageLabel(app)
#scav.pack(padx=10, pady=10)
#scav.load('scav.gif')
#scav.place(x= 650, y=50)

app.mainloop()