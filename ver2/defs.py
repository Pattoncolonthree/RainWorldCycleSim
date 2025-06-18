#imports and set ups
import time
import random
import sys
import winsound
import threading
import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
from itertools import count
import winsound
#imports
#defining global variables 
has_spear = True
has_rock = False
aggression = 1
seconds = time.time()
local_time = time.ctime(seconds)
creature = "rainworl"
attack = "wow murders u or smth"
answer = None
weapon = "placeholder"
runaway = False

#Temporary code
def spearchance():
    return random.randint(1,2)

if spearchance() == 1:
    has_spear = True
else:
    has_spear = False
#

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
#this function is because while using gifs if i am to use the time.sleep for long periods of time, the gifs wont update their frames at all during that time
#so this just makes it so that i can update the gifs(so they dont just suddenly stop) while also having a pause for other parts of the code ^_^

def printString(string):
    for char in string:
        Label.configure(text=Label.cget('text') + char, font=('Arial', 18, 'bold'), fg="#d1cdf0", bg="#180821")
        Label.update()
        time.sleep(0.0625)
    sleepy()
    text = Label.configure(text= " ")
    Label.update
#delays each letter of the sentence to get a cleaner look.
#whatever is in the delay_print brackets will be printed one at a time on the speed stated in the time.sleep
   


Label = tk.Label(app)
Label.pack(padx=10, pady=10)
Label.place(x= 110, y= 575)

ImageLabel(bg="#180821")
slug = ImageLabel(app, borderwidth = 0)
slug.pack(padx=10, pady=10)
slug.load('scavandscug.gif')
slug.place(x= 0, y=0)


def attackchance():
    return random.randint(1,2)
#seeing the chances of if the player hits when they throw weapon

def check():
    time.sleep(10)
    if answer != None:
        return
        text:(f"you panic not responding in time as The Lizard sinks it's teeth into you")
        printString(text)
        quit()


def reputation(aggression):
    if has_spear == True:
        aggression += 2
    if has_rock == True:
        aggression += 1
    
    return aggression
#adding the reputation system base, in the main code extra things will make the aggression go up.

def reputationrng():
    return random.randint(reputation(aggression), reputation(aggression) + 5)
#will check this !!!!!!! dunno if it works
#code is to make a random number based on the level of aggression from the scavenger
# The code will be used for when the aggression is higher, the chance of the scavenger attacking is higher.


def callalldefs():
    attackchance()
    reputation(aggression)
    reputationrng()
    