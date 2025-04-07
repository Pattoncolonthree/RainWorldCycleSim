#imports and set ups
import time
import random
import sys
#imports


aggression = 1
has_spear = False
has_rock = False
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


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
#delays each letter of the sentence to get a cleaner look.

def attackchance():
    return random.int(1,2,3)
#seeing the chances of if the player hits when they 


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
    return random.int({aggression}, {aggression + 5})
    #will check this !!!!!!! dunno if it works
#code is to make a random number based on the level of aggression from the scavenger
# The code will be used for when the aggression is higher, the chance of the scavenger attacking is higher.

def scavenger():
   
    delay_print("You look towards the creature in front of you, it looks back at you, it's quills spiking up.\n")
    time.sleep(2)
    if reputation(aggression) <= 1:
        delay_print("The Scavenger looks at you warily, clutching it's spear to it's chest protectively\n")
    elif reputation(aggression) > 1 and reputation(aggression) <= 3:
        delay_print("The Scavenger raises it's spear towards you, but seems more defensive than offensive\n")
    else:
        delay_print("The Scavenger frills up, raising it's spear, and you know it intends to use it.\n")

    if has_spear == True or has_rock == True:
            delay_print(f"You look warily at the Scavenger, raising your own {weapon} defensively\n")
            print(" ")
            delay_print(f"You think of your options. Throw the {weapon} at it? Drop the weapon for peace??\n")
            print(" ")
            action = input("What do you do? ").lower()
            if action == "throw" or action == "throw spear" or action == "attack":
                if attackchance() == 3:
                    if reputationrng() < 3:
                        delay_print("The scavenger jumps out of the way, scrambling to it's feet and staring at you\n")
                        time.sleep(2)
                        print(" ")
                        time.sleep(2)
                        delay_print("Without another thought the scavenger dives towards a tunnel, squeezing through and running away\n")
                        runaway = True
                    elif reputationrng > 3:
                        delay_print("The scavenger jumps out of the way, scrambling to it's feet and staring at you\n")
                        time.sleep(2)
                        print(" ")
                        time.sleep(2)
                        delay_print("The creature's spikes slowly rise as it turns to you\n")
                    



print(scavenger())