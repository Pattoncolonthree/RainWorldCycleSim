from test3gui import *
import tkinter as tk
from tkinter import *
import time
import os
from PIL import Image, ImageTk
from itertools import count
import winsound
from GUICreatureInteractions import *




if has_spear == False:
    scavscug = ImageLabel(app, borderwidth = 0)
    scavscug.pack(padx=10, pady=10)
    scavscug.load('scavandscug.gif')
    scavscug.place(x= 0, y=0)
else:
    scavscugsp = ImageLabel(app, borderwidth = 0)
    scavscugsp.pack(padx=10, pady=10)
    scavscugsp.load('scavandscugspear.gif')
    scavscugsp.place(x= 0, y=0)

scavdodgerun = ImageLabel(app, borderwidth = 0)
scavdodgerun.pack(padx=10, pady=10)
scavdodgerun.place(x= 0, y=0)

scug = ImageLabel(app, borderwidth = 0)
scug.pack(padx=10, pady=10)
scug.place(x= 0, y=0)