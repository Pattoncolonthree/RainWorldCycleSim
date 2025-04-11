#imports and set ups
from Creatureinteractions import *
from test3gui import *

has_spear = True
has_rock = False

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
        text = ("The Scavenger looks at you warily, clutching it's spear to\nit's chest protectively\n")
        printString(text)
    elif reputation(aggression) > 1 and reputation(aggression) <= 3:
        text = ("The Scavenger raises it's spear towards you, but seems more\ndefensive than offensive\n")
        printString(text)
    else:
        text = ("The Scavenger frills up, raising it's spear, and you know\nit intends to use it.\n")
        printString(text)
    if has_spear == True or has_rock == True:
            text = (f"You look warily at the Scavenger, raising your own {weapon} defensively\n")
            printString(text)
            text = (f"You think of your options. Throw the {weapon} at it?\nDrop the weapon for peace??\n")
            printString(text)
            action = input("What do you do? ").lower()
            if action == "throw" or action == "throw spear" or action == "attack":
                if attackchance() <= 2:
                    if reputationrng() <= 10:
                        slug.load('scavdodgerun.gif')
                        text = ("The scavenger jumps out of the way, scrambling to it's feet and staring at you\n")
                        printString(text)
                        text = ("Without another thought the scavenger dives towards a tunnel, squeezing through and running away\n")
                        printString(text)
                        slug.load('scug.gif')
                        runaway = True
                    elif reputationrng() > 11:
                        text = ("The scavenger jumps out of the way, scrambling to it's feet and staring at you\n")
                        printString(text)
                        text = ("The creature's spikes slowly rise as it turns to you\n")
                        printString(text)
                        text = ("It raises it's spear to you\n")
                        printString(text)
                        if attackchance() == 2:
                            text = ("...")
                            longprintString(text)
                            text = ("The spear clanks to the ground next to you")
                            printString(text)
                            text = ("O_O'")
                            longprintString(text)
                            text = ("You and the Scavenger stare at eachother for a moment")
                            printString(text)
                            text = ("It takes a small step to the side")
                            printString(text)
                            text = ("The Scavenger then sprints in to the tunnel next to it")
                            printString(text)
                            text = ("(You get the distinct thought that the Scavenger was embarrassed)")
                        else:
                            text = ("...\n")
                            longprintString(text)
                            text = ("The spear stabs right through your chest.\n")
                            printString(text)
                            text = ("The last thing you see before your vision goes black is the Scavenger running off")
                            printString(text)
                            text = ("YOU DIED")
                            
                            winsound.PlaySound('death.wav', winsound.SND_FILENAME)
                    else:
                        text = ("what,,,,,")
                        printString(text)
                else:
                    text = ("The spear peirces the Scavengers chest")
                    printString(text)
                    text = ("The creature doesn't even get a chance to react before it has already collapsed\n")
                    printString(text)









print(scavgui())


app.mainloop()