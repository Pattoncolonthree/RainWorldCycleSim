#imports and set ups
import time
import random
import sys
import winsound
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

def attackchance():
    return random.randint(1,3)
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
    return random.int({aggression}, {aggression + 5})
    #will check this !!!!!!! dunno if it works
#code is to make a random number based on the level of aggression from the scavenger
# The code will be used for when the aggression is higher, the chance of the scavenger attacking is higher.


def scavenger():
    winsound.PlaySound('threat.wav', winsound.SND_FILENAME,) 
    winsound.SND_ASYNC
    delay_print("You look towards the creature in front of you, it looks back at you, it's quills spiking up.\n")
    time.sleep(2)
    print(" ")
    if reputation(aggression) <= 1:
        delay_print("The Scavenger looks at you warily, clutching it's spear to it's chest protectively\n")
    elif reputation(aggression) > 1 and reputation(aggression) <= 3:
        delay_print("The Scavenger raises it's spear towards you, but seems more defensive than offensive\n")
    else:
        delay_print("The Scavenger frills up, raising it's spear, and you know it intends to use it.\n")

    if has_spear == True or has_rock == True:
            time.sleep(2)
            print(" ")
            delay_print(f"You look warily at the Scavenger, raising your own {weapon} defensively\n")
            time.sleep(2)
            print(" ")
            delay_print(f"You think of your options. Throw the {weapon} at it? Drop the weapon for peace??\n")
            time.sleep(2)
            print(" ")
            action = input("What do you do? ").lower()
            if action == "throw" or action == "throw spear" or action == "attack":
                if attackchance() == 3:
                    if reputationrng() <= 3:
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
                        time.sleep(2)
                        print(" ")
                        delay_print("It raises it's spear to you\n")
                        time.sleep(2)
                        print(" ")
                        if attackchance() == 3:
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
                            time.sleep(2)
                            print(" ")
                            delay_print("The last thing you see before your vision goes black is the Scavenger running off ")
                            bigdelay_print("YOU DIED")
                            winsound.PlaySound('death.wav', winsound.SND_FILENAME)
                else:
                    delay_print("The spear peirces the Scavengers chest")
                    time.sleep(2)
                    print(" ")
                    delay_print("The creature doesn't even get a chance to react before it has already collapsed")




                    


print(scavenger())
