import time
from threading import Thread
seconds = time.time()
local_time = time.ctime(seconds)

print("Monk is easy, Survivor is normal and Hunter is hard mode.")
slug = input("What slugcat are you playing? ")
slugcat = slug.lower()
choice_made = False


while choice_made == False:
    if slugcat == "monk":
        print("Weak of body but strong in spirit. In tune with the mysteries of the world and empathetic to its creatures, your journey will be a significantly more peaceful one")
        time.sleep(3)
        print("They are physically weaker than  Survivor, but predators are less frequent and less aggressive, making the world comparatively easier to traverse.")
        choice_made = True
    elif slugcat == "survivor":
        print("A nimble omnivore, both predator and prey. Lost in a harsh and indifferent land you must make your own way, with wit and caution as your greatest assets.")
        time.sleep(3)
        print("The Survivor must deal with the ever-present threat of predators while trying to find their way through this hostile world. Survivor has standard Slugcat stats and abilities.")
        choice_made = True
    elif slugcat == "hunter":
        print("Strong and quick, with a fierce metabolism requiring a steady diet of meat. But the stomach won't be your only concern, as the path of the hunter is one of extreme peril.")
        time.sleep(3)
        print("Though they are faster and stronger than  Survivor, their campaign features a multitude of changes to make the game much more challenging.")
        choice_made = True
    else:   
        print("That is not available, Choose from Survivor, Monk or Hunter")
        slugcat = input("What slugcat are you playing? ").lower()
time.sleep(10)
print(" ")
#I hate loops omfg
#someones dying and it aint gon be a slugcat
if slugcat == "monk":
    print("You traverse through outskirts in search of Survivor")
    time.sleep(1)
    print(" ")
    time.sleep(2)
    print("while you warily walk into an abandoned building, a Pink Lizard stares back at you, hissing slightly")
    print(" ")
    time.sleep(2)




answer = None

def check():
    time.sleep(10)
    if answer != None:
        return
    print("You panic, taking too long to respond. The Pink Lizard snarls and pounces on you. Killing you.")
    exit

Thread(target = check).start()

answer = input("Quick! there is a SPEAR, a ROCK or TUNNEL. What do you do? ").lower()
print(" ")


throw = None
spear = None
tunnel = None

if answer == "rock":
    print("you dive for the rock near you picking it up shakily as you face the lizard, who has now taken a step towards you")
    def check():
        time.sleep(5)
        if throw != None:
            return
        print("You panic, taking too long to respond. The Pink Lizard snarls and pounces on you. Killing you.")
        exit
    Thread(target = check).start()
    throw = input("Quick! Where do you Throw it?! WALL(distract it!), LIZARD(Hit him right in the jaws!) ").lower()
    time.sleep(1)
    print(" ")
    time.sleep(1)
    print(" ")
    time.sleep(1)
    if throw == "wall":
        print("The Lizard pauses for a second, looking at the wall for a second with a slightly dumbstruck expression")
        time.sleep(3)
        print("You have the suspision it's disapointed in your attempts, but your thoughts are cut short as it pounces on you. Killing you instantly")
        time.sleep(3)
        exit
    elif throw == "lizard":
        print("The Lizard shakes it's head, disoriented")
        time.sleep(1)
        print("You take the oportunity to run, getting away while the lizard was distracted.")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)

elif answer == "spear":
    print("You grab the spear in front of you, shakily holding it up to the lizard")
    def check():
        time.sleep(5)
        if spear != None:
            return
        print("You panic, taking too long to respond. The Pink Lizard snarls and pounces on you. Killing you.")
        exit
    Thread(target = check).start()
    spear = input("Quick! Where do you Throw it?! SIDE(stab the side), FACE(Hit him right in the jaws!) ").lower()
    time.sleep(1)
    print(" ")
    time.sleep(1)
    print(" ")
    time.sleep(1)
    if spear == "face":
        print("You throw the spear at the lizards face. The spear bounces off and it shakes it's unharmed jaws")
        time.sleep(2)
        print(" ")
        time.sleep(2)
        print("The lizard snarls, now visibly angrier. It crushes you in it's jaws, killing you instantly")
        time.sleep(2)
        print(" ")
        time.sleep(2)
        exit

    elif spear == "side":
        print("You swiftly stab the lizard in it's side, causing it to call out in pain")
        time.sleep(2)
        print(" ")
        time.sleep(2)
        print("While the Lizard is disorientated and hurt, you flee from the room.")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)

elif answer == "tunnel":
    print("You quickly back into the tunnel you came from, hoping the lizard didnt notice you(it did)")
    time.sleep(3)
    print("you jump out the tunnel but hear an unfortunate noise behind you")
    def check():
        time.sleep(5)
        if tunnel != None:
            return
        print("You panic, taking too long to respond. The Pink Lizard snarls and pounces on you. Killing you.")
        exit
    Thread(target = check).start()
    tunnel = input("Quick! What do you do?!RUN(turn and sprint away!) or play DEAD(maybe it wont eat you?)").lower()
    if tunnel == "DEAD":
        time.sleep(2)
        print(" ")
        time.sleep(2)
        print(" ")
        time.sleep(1)
        print("The Lizard springs out of the tunnel! Ready to chase you and..!")
        time.sleep(4)
        print(". ")
        time.sleep(.5)
        print(".. ")
        time.sleep(.5)
        print("...")
        time.sleep(3)
        print("It looks down at you with an expression of bewildered satisfaction")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("The Pink lizard crushes you in it's jaws, turning your fake death real.")
        time.sleep(2)
        print(" ")
        exit
    elif tunnel == "run":
        time.sleep(2)
        print(" ")
        time.sleep(2)
        print(" ")
        time.sleep(1)
        print("You dont even turn to face it before sprinting away.")
        time.sleep(4)
        print("tap")
        time.sleep(.5)
        print("Clink!")
        time.sleep(.5)
        print("THUMP!")
        time.sleep(1)
        print("You didnt stop till the lizard sounds were far gone. You stopped to breath, before looking around the new room")


    
    elif tunnel == "run":
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)

else:
    print("That's not an option! The pink Lizard pounces on you, killing you insantly")
    exit