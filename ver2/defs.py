# imports and set ups
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


# imports
# Initialising global variables
has_spear = False
has_rock = False
aggression = 1
seconds = time.time()
local_time = time.ctime(seconds)
creature = "rainworl"
attack = "wow murders u or smth"
answer = None
weapon = "placeholder"
runaway = False

class App(tk.Tk):
    """
   
    """
    def __init__(self):
       super().__init__()


app = App()
app.geometry("1006x700")
app.title("Cycle sim")
app.configure(background='#180821')


# I have taken and adjusted the following Class code for my own code.
# sourced from:
# https://stackoverflow.com/questions/43770847/play-an-animated-gif-in-python-with-tkinter


class ImageLabel(tk.Label):
    """A label which displays images and plays them if they are gifs.

    This Widget will load an image from a file path or PIL image object.
    if the image is a gif, it will automatically play in sequence.
    """
    def load(self, im):
        """Load an image or a gif into the Label.

        This function handles:
            -For static images, the function will just load the image
            -for gifs it will break down the gifs into frames and their timings
            and then play them in sequence.
        """
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
# wwwwwwwwwwwwwwwwwwwww


def sleepy():
    """repeats sleep for 0.05 seconds for the amount of characters in 'length'.
    """
    for char in length:
        time.sleep(0.05)
        Label.update()
# this function is because while using gifs if i am to use the time.sleep for long periods of time, the gifs wont update their frames at all during that time
# so this just makes it so that i can update the gifs(so they dont just suddenly stop) while also having a pause for other parts of the code ^_^


# Temporary code
def spear_chance():
    """this code will randomise with either 1 or 2 and return the output.
    """
    return random.randint(1,2)


if spear_chance() == 1:
    has_spear = True
else:
    has_spear = False
# 


def print_string(string):
    """
    
    """
    for char in string:
        Label.configure(text=Label.cget('text') + char, font=('Arial', 18, 'bold'), fg="#d1cdf0", bg="#180821")
        Label.update()
        time.sleep(0.0625)
    sleepy()
    text = Label.configure(text= " ")
    Label.update
# delays each letter of the sentence to get a cleaner look.
# whatever is in the delay_print brackets will be printed one at a time on the speed stated in the time.sleep


Label = tk.Label(app)
Label.pack(padx=10, pady=10)
Label.place(x= 110, y= 575)



def attack_chance():
    """
    
    """
    return random.randint(1,2)
# seeing the chances of if the player hits when they throw weapon


def check():
    """
    
    """
    time.sleep(10)
    if answer != None:
        return
        text:(f"you panic not responding in time as The Lizard sinks it's teeth into you")
        print_string(text)
        quit()
# 18/06/2025 -Code above isnt used in what i have so far in my Program, but is set up for my future additions.


def reputation(aggression):
    """
    
    """
    if has_spear is True:
        aggression += 2
    if has_rock is True:
        aggression += 1
    return aggression
# adding the reputation system base, in the main code extra things will make the aggression go up.


def reputation_rng():
    """
    
    
    """
    return random.randint(reputation(aggression), reputation(aggression) + 5)
# will check this !!!!!!! dunno if it works
# code is to make a random number based on the level of aggression from the scavenger
# The code will be used for when the aggression is higher, the chance of the scavenger attacking is higher.


def call_all_defs():
    attack_chance()
    reputation(aggression)
    reputation_rng()
