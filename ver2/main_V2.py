import tkinter as tk
from tkinter import *
import time
import os
from PIL import Image, ImageTk
from itertools import count
import winsound
import GUI_Creature_Interactions as ci

"""Main program, calls scav_GUI code and plays it.
"""


ci.scav_gui()

ci.app.mainloop()