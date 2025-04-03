#imports and set ups
import time
aggression = 1
has_spear = True


has_rock = True
seconds = time.time()
local_time = time.ctime(seconds)
creature = "rainworl"
attack = "wow murders u or smth"
answer = None
weapon = "placeholder"
if has_spear == True:
    weapon = "Spear"
if has_rock == True:
    weapon = "Rock"
if has_rock == True and has_spear == True:
    weapon = "Spear and rock"


def check():
    time.sleep(10)
    if answer != None:
        return
    print(f"you panic not responding in time as {creature} {attack}")
    quit()

def reputation(aggression):
    if has_spear == True:
        aggression += 2
    if has_rock == True:
        aggression += 1

def scavenger(scav):
   
    print("You look towards the creature in front of you, it looks back at you, it's quills spiking up.")
    time.sleep(2)
    if reputation <= 1:
        print("The Scavenger looks at you warily, clutching it's spear to it's chest protectively")
    elif reputation > 1 and reputation <= 3:
        print("The Scavenger raises it's spear towards you, but seems more defensive than offensive")
    else:
        print("The Scavenger frills up, raising it's spear, and you know it intends to use it.")

    if reputation <= 1:
        if has_spear == True or has_rock == True:
            print("You look warily at the Scavenger, raising your own {weapon} defensively")
            print("You think of your options. Throw the spear? drop the we")
            action = input("")
            

    
    
     

    



