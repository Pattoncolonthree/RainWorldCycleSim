#imports and set ups
import time
import random
import sys
import winsound
import threading
#imports

aggression = 1
has_spear = True
has_rock = True
seconds = time.time()
local_time = time.ctime(seconds)
creature = "rainworl"
attack = "wow murders u or smth"
answer = None
weapon = "placeholder"
runaway = False
if has_spear == True:
    weapon = "Spear"
if has_rock == True:
    weapon = "Rock"
if has_rock == True and has_spear == True:
    weapon = "Spear and rock"

def bigdelay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1)

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
#delays each letter of the sentence to get a cleaner look.
#whatever is in the delay_print brackets will be printed one at a time on the speed stated in the time.sleep

def attackchance():
    return random.randint(1,2)
#seeing the chances of if the player hits when they throw weapon


def check():
    time.sleep(10)
    if answer != None:
        return
    delay_print(f"you panic not responding in time as {creature} {attack}\n")
    quit()


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

def scavenger():
    winsound.PlaySound('threat.wav', winsound.SND_ASYNC)
    #winsound!!!! will play the audio as the gameplays and will loop! playing any other sound cancels this but i am gonna attempt to fix this :3
    #I HAVE PERMISSION FROM RIVOTTER AND JAMES THERRIAN(James Primate) TO USE BOTH THE MUSIC AND AUDIO FROM THE GAME: Rain World by Video Cult
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
    
                    








                


print("woah u at the end")