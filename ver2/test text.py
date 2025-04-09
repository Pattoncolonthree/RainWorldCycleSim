from Creatureinteractions import *
import tkinter as tk
from tkinter import *
import time
import os
from PIL import Image, ImageTk
from itertools import count



def printString(string):
    for char in string:
        Label.configure(text=Label.cget('text') + char)
        Label.update()
        time.sleep(.25)

app = tk.Tk()

app.geometry("900x600")
app.title("ending my life!!!!")
app.configure(background='#eeefff')
text = "Hello world!"
Label = tk.Label(app)
Label.pack(padx=10, pady=10)
printString(text)
app.mainloop()





def hi():
    delay_print("You look towards the creature in front of you, it looks back at you, it's quills spiking up.\n")
    time.sleep(0.5)
    print(" ")
    time.sleep(0.5)
    if reputation(aggression) <= 1:
        delay_print("The Scavenger looks at you warily, clutching it's spear to it's chest protectively\n")
    elif reputation(aggression) > 1 and reputation(aggression) <= 3:
        delay_print("The Scavenger raises it's spear towards you, but seems more defensive than offensive\n")
    else:
        delay_print("The Scavenger frills up, raising it's spear, and you know it intends to use it.\n")
    if has_spear == True or has_rock == True:
            time.sleep(0.5)
            print(" ")
            time.sleep(0.5)
            delay_print(f"You look warily at the Scavenger, raising your own {weapon} defensively\n")
            time.sleep(0.5)
            print(" ")
            time.sleep(0.5)
            delay_print(f"You think of your options. Throw the {weapon} at it? Drop the weapon for peace??\n")
            time.sleep(0.5)
            print(" ")
            time.sleep(0.5)
            action = input("What do you do? ").lower()
            if action == "throw" or action == "throw spear" or action == "attack":
                if attackchance() == 2:
                    if reputationrng() <= 5:
                        delay_print("The scavenger jumps out of the way, scrambling to it's feet and staring at you\n")
                        time.sleep(0.5)
                        print(" ")
                        time.sleep(0.5)
                        delay_print("Without another thought the scavenger dives towards a tunnel, squeezing through and running away\n")
                        runaway = True
                    elif reputationrng() > 6:
                        delay_print("The scavenger jumps out of the way, scrambling to it's feet and staring at you\n")
                        time.sleep(0.5)
                        print(" ")
                        time.sleep(0.5)
                        delay_print("The creature's spikes slowly rise as it turns to you\n")
                        time.sleep(0.5)
                        print(" ")
                        time.sleep(0.5)
                        delay_print("It raises it's spear to you\n")
                        time.sleep(0.5)
                        print(" ")
                        time.sleep(0.5)
                        if attackchance() == 2:
                            bigdelay_print("...\n")
                            delay_print("The spear clanks to the ground next to you\n")
                            bigdelay_print("O_O'\n")
                            delay_print("You and the Scavenger stare at eachother for a moment\n")
                            time.sleep(2)
                            print(" ")
                            delay_print("It takes a small step to the side\n")
                            time.sleep(2)
                            print(" ")
                            delay_print("The Scavenger then sprints in to the tunnel next to it\n")
                            time.sleep(2)
                            print(" ")
                            delay_print("(You get the distinct thought that the Scavenger was embarrassed)")
                        else:
                            bigdelay_print("...\n")
                            delay_print("The spear stabs right through your chest.\n")
                            time.sleep(0.5)
                            print(" ")
                            time.sleep(0.5)
                            delay_print("The last thing you see before your vision goes black is the Scavenger running off \n")
                            delay_print("YOU DIED\n")
                            winsound.PlaySound('death.wav', winsound.SND_FILENAME)
                    else:
                        print("what,,,,,")
                else:
                    delay_print("The spear peirces the Scavengers chest")
                    time.sleep(0.5)
                    print(" ")
                    time.sleep(0.5)
                    delay_print("The creature doesn't even get a chance to react before it has already collapsed\n")