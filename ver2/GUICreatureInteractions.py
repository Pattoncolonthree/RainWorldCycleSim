#imports and set ups

has_rock = False

import time
import random
import sys
import winsound
import threading
from test3gui import *
from test4gifs import *
from defs import *

def spearchance():
    return random.randint(1,2)

if spearchance() == 1:
    has_spear = True
else:
    has_spear = False

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

spike = ImageLabel(app, borderwidth = 0)
spike.pack(padx=10, pady=10)
spike.place(x= 0, y=0)

spiked = ImageLabel(app, borderwidth = 0)
spiked.pack(padx=10, pady=10)
spiked.place(x= 0, y=0)

scavmiss = ImageLabel(app, borderwidth = 0)
scavmiss.pack(padx=10, pady=10)
scavmiss.place(x= 0, y=0)

scug = ImageLabel(app, borderwidth = 0)
scug.pack(padx=10, pady=10)
scug.place(x= 0, y=0)

scavkill = ImageLabel(app, borderwidth = 0)
scavkill.pack(padx=10, pady=10)
scavkill.place(x= 0, y=0)

rahh = ImageLabel(app, borderwidth = 0)
rahh.pack(padx=10, pady=10)
rahh.place(x= 0, y=0)

def attackchance():
    return random.randint(1,2)

def reputation(aggression):
    if has_spear == True:
        aggression += 2
    if has_rock == True:
        aggression += 1
    return aggression
#adding the reputation system base, in the code extra things will make the aggression go up.

def reputationrng():
    return random.randint(reputation(aggression), reputation(aggression) + 5)
    #will check this !!!!!!! dunno if it works
#code is to make a random number based on the level of aggression from the scavenger
# The code will be used for when the aggression is higher, the chance of the scavenger attacking is higher.


def scavgui():
    winsound.PlaySound('threat.wav', winsound.SND_ASYNC)
    #winsound!!!! will play the audio as the gameplays and will loop! playing any other sound cancels this but i am gonna attempt to fix this :3
    #I HAVE PERMISSION FROM RIVOTTER AND JAMES THERRIAN(James Primate) TO USE BOTH THE MUSIC AND AUDIO FROM THE GAME: Rain World by Video Cult                                                                                                                   
    text = ("You look towards the creature in front of you, it looks back at you.\n It's quills spike up.")
    printString(text)
    if reputation(aggression) <= 1:
        text = ("The Scavenger looks at you warily, clutching it's spear to\nit's chest protectively  ")
        printString(text)
    elif reputation(aggression) > 1 and reputation(aggression) <= 3:
        text = ("The Scavenger raises it's spear towards you, but seems more\ndefensive than offensive")
        printString(text)
    else:
        text = ("The Scavenger frills up, raising it's spear, and you know\nit intends to use it.")
        printString(text)
    if has_spear == True or has_rock == True:
        text = (f"You look warily at the Scavenger, raising your own Spear defensively")
        printString(text)
        text = (f"You think of your options. Throw the Spear at it?\nDrop the weapon for peace??")
        printString(text)
        action = input("What do you do? ").lower()
        if action == "throw" or action == "throw spear" or action == "attack":
            if attackchance() <= 2:
                if reputationrng() <= 0:
                    scavdodgerun.load('scavdodgerun.gif')
                    text = ("The scavenger jumps out of the way, scrambling to it's feet and staring at you")
                    printString(text)
                    text = ("Without another thought the scavenger dives towards a tunnel, squeezing through and running away")
                    printString(text)
                    scavscugsp.load('scug.gif')
                    runaway = True
                elif reputationrng() > 0:
                    spike.load('spikeup.gif')
                    text = ("The scavenger jumps out of the way, scrambling to it's feet and staring at you")
                    printString(text)
                    spiked.load('spikedup.gif')
                    text = ("It raises it's spear to you")
                    printString(text)
                    if attackchance() > 2:
                        text = ("...")
                        printString(text)
                        scavmiss.load('scavmiss.gif')
                        text = ("The spear clanks to the ground next to you")
                        printString(text)
                        text = ("O_O'")
                        printString(text)
                        text = ("The Scavenger sprints in to the tunnel next to it")
                        printString(text)
                        text = ("(You get the distinct thought that the Scavenger was embarrassed)")
                    else:
                        text = ("...")
                        printString(text)
                        scavmiss.load('scavhit.gif')
                        text = ("The spear stabs right through your chest.")
                        printString(text)
                        text = ("The last thing you see before your vision goes black \n is the Scavenger running off")
                        printString(text)
                        rahh.load('black.gif')
                        text = ("YOU DIED")
                        printString(text)
                        winsound.PlaySound('death.wav', winsound.SND_FILENAME)
                        time.sleep(5)
                        quit
                else:
                    text = ("what,,,,,")
                    printString(text)
            else:
                text = ("The spear peirces the Scavengers chest")
                printString(text)
                text = ("The creature doesn't even get a chance to react before it has already collapsed\n")
                printString(text)
        elif action == "drop" or action == "drop spear" or action == "peace":
            text = ("You slowly toss the spear away from yourself")
            printString(text)
            rahh.load('scavandscug')
            print(reputation(aggression))
            text = ("The scavenger blinks at you, lowering it's own spear")
            printString(text)

    else:
        text = ("You look warily at the Scavenger, seeing it's armed with a spear")
        printString(text)
        text = ("you think of your options. Try to run past? maybe crouch to show you aren't a threat")










print(scavgui())


app.mainloop()