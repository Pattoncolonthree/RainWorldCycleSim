#imports and set ups
import time
import random
import sys
import winsound
import threading
#imports

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
