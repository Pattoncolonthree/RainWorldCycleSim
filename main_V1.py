import time
from threading import Thread
seconds = time.time()
local_time = time.ctime(seconds)

print("Monk is easy, Survivor is normal and Hunter is hard mode.")
slugcat = input("What slugcat are you playing? ").lower()
choice_made = False

foodpips = int("1")


while choice_made == False:
    if slugcat == "monk":
        print("Weak of body but strong in spirit. In tune with the mysteries of the world and empathetic to its creatures, your journey will be a significantly more peaceful one")
        time.sleep(3)
        print("They are physically weaker than  Survivor, but predators are less frequent and less aggressive, making the world comparatively easier to traverse.")
        choice_made = True
        #Monk is the only working one rn so yeah uhm
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

#the blank prints and sleeps to make stuff not go too fast and look nicer(with all the lines too close it feels very busy)

#I honestly think that i'm gonna instead of so many time.sleep(x)'s Im gonna make some of the prints into inputs
#^^^^so that the user can choose when to skip dialogue(especially on replays, and when you've died and restarted, waiting over and over gets frustrating)


answer = None

#first function, adjusted from stack overflow (https://stackoverflow.com/questions/15528939/time-limited-input)
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
<<<<<<< HEAD
        time.sleep(3)
        print(" ")
        print("you look behind yourself warily, but the lizard is nowhere in sight. You sigh in relief")
=======
>>>>>>> ab9020bc085e63ba36bed61910f1d02620daf6b6
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
<<<<<<< HEAD
    else:
        print("That's not an option! The pink Lizard pounces on you, killing you insantly") 
        exit
#adding timed events in order to make the situations more tense ^_^

=======
>>>>>>> ab9020bc085e63ba36bed61910f1d02620daf6b6

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
<<<<<<< HEAD
        print("The Spear hits the lizards face, bouncing off as the lizard hisses, shaking it's unharmed face.")
        time.sleep(2)
        print(" ")
        time.sleep(2)
        print("The Lizard looks at you, now undeniably furious. It snarls and pounces, crushing you in it's jaws.")
        time.sleep(3)
        exit
    elif spear == "side":
        print("You stab the lizard in it's side hastily, and while the creature writhes, you take the chance to run")
        time.sleep(3)
        print(" ")
        print("you look behind yourself warily, but the lizard is nowhere in sight. You sigh in relief")
=======
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
>>>>>>> ab9020bc085e63ba36bed61910f1d02620daf6b6
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
<<<<<<< HEAD
    else:
        print("That's not an option! The pink Lizard pounces on you, killing you insantly") 
        exit
=======
>>>>>>> ab9020bc085e63ba36bed61910f1d02620daf6b6

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
<<<<<<< HEAD
    if tunnel == "dead":
        print("The lizard jumps out of the tunnel, ready to give chase!")
        time.sleep(2)
        print("It pauses before slowly looking down at you")
        time.sleep(2)
        print("Only a moment later, the Lizards jaws chomp down on you. It was gonna kill you anyway, why did you think that would work?")
        time.sleep(3)
        exit
    elif tunnel == "run":
        print("You zip off! Not even looking back at the Lizard behind you as you jump and dive between the obsticles in your way. Finally you dive into a tunnel leading into another room.")
        time.sleep(2)
        print(" ")
        time.sleep(2)
        print("you look behind yourself warily, but the lizard is nowhere in sight. You sigh in relief")
=======
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
>>>>>>> ab9020bc085e63ba36bed61910f1d02620daf6b6

else:
    print("That's not an option! The pink Lizard pounces on you, killing you insantly") 
    exit

roomchoice = False
print("You look around the room you now find yourself in")
time.sleep(1)
print(" ")
time.sleep(1)
print("There is a tunnel into another room and a few berries")
print(" ")
time.sleep(1)
print(" ")
time.sleep(1)
room = input("what do you go to? ").lower()


while roomchoice == False:
    if room == "berry" or "berries":
        print("You walk up to the berries, there are three of them")
        amount = input(int("How many do you eat? "))
        try:
            amount += 1
        except TypeError:
            amount = input(int("that's not a number. How many do you eat? "))