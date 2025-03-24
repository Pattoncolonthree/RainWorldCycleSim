#first function, adjusted from stack overflow (https://stackoverflow.com/questions/15528939/time-limited-input)
def check():
    time.sleep(10)
    if answer != None:
        return
    print("You panic, taking too long to respond. The Pink Lizard snarls and pounces on you. Killing you.")
    quit()


import time
from threading import Thread
from functest1 import *

seconds = time.time()
local_time = time.ctime(seconds)
score = int("0")

print("Monk is easy, Survivor is normal and Hunter is hard mode.(Only Monk available at the moment.)")
time.sleep(1)
print(" ")
time.sleep(1)
slugcat = input("What slugcat are you playing? ").lower()
choice_made = False

foodpips = int("1")


while choice_made == False:
    if slugcat == "monk":
        input("Weak of body but strong in spirit. In tune with the mysteries of the world and empathetic to its creatures, your journey will be a significantly more peaceful one ")
        input("They are physically weaker than  Survivor, but predators are less frequent and less aggressive, making the world comparatively easier to traverse. ")
        choice_made = True
        #Monk is the only working one rn so yeah uhm
    elif slugcat == "survivor":
        input("A nimble omnivore, both predator and prey. Lost in a harsh and indifferent land you must make your own way, with wit and caution as your greatest assets. ")
        input("The Survivor must deal with the ever-present threat of predators while trying to find their way through this hostile world. Survivor has standard Slugcat stats and abilities. ")
        choice_made = True
    elif slugcat == "hunter":
        input("Strong and quick, with a fierce metabolism requiring a steady diet of meat. But the stomach won't be your only concern, as the path of the hunter is one of extreme peril. m")
        input("Though they are faster and stronger than  Survivor, their campaign features a multitude of changes to make the game much more challenging. ")
        choice_made = True
    else:   
        print("That is not available, Choose from Survivor, Monk or Hunter")
        slugcat = input("What slugcat are you playing? ").lower()
#Getting player to choose what campaign they want to play as then telling them about the campaign.

time.sleep(1)
print(" ")
time.sleep(1)
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
else:
    print("uhm....... you arent supposed to do that,,,,,,,,, uh bye")
    quit()
#setting up slugcat starting place, story and first enemy.

#the blank prints and sleeps to make stuff not go too fast and look nicer(with all the lines too close it feels very busy)

#I honestly think that i'm gonna instead of so many time.sleep(x)'s Im gonna make some of the prints into inputs
#^^^^so that the user can choose when to skip dialogue(especially on replays, and when you've died and restarted, waiting over and over gets frustrating)

answer = None

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
        quit()
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
        quit()
    elif throw == "lizard":
        print("The Lizard shakes it's head, disoriented")
        time.sleep(1)
        print("You take the oportunity to run, getting away while the lizard was distracted.")
        score = (score + 1)

        time.sleep(3)
        print(" ")
        print("you look behind yourself warily, but the lizard is nowhere in sight. You sigh in relief")

        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)

    else:
        print("That's not an option! The pink Lizard pounces on you, killing you insantly") 
        quit()
#Option 1= rock, gives all the options for if player picks 'rock'
#adding timed events in order to make the situations more tense ^_^



elif answer == "spear":
    print("You grab the spear in front of you, shakily holding it up to the lizard")
    def check():
        time.sleep(5)
        if spear != None:
            return
        print("You panic, taking too long to respond. The Pink Lizard snarls and pounces on you. Killing you.")
        quit()
    Thread(target = check).start()
    spear = input("Quick! Where do you Throw it?! SIDE(stab the side), FACE(Hit him right in the jaws!) ").lower()
    time.sleep(1)
    print(" ")
    time.sleep(1)
    print(" ")
    time.sleep(1)
    if spear == "face":
        print("The Spear hits the lizards face, bouncing off as the lizard hisses, shaking it's unharmed face.")
        time.sleep(2)
        print(" ")
        time.sleep(2)
        print("The Lizard looks at you, now undeniably furious. It snarls and pounces, crushing you in it's jaws.")
        time.sleep(3)
        quit()
    elif spear == "side":
        print("You stab the lizard in it's side hastily, and while the creature writhes, you take the chance to run")
        time.sleep(3)
        print(" ")
        print("you look behind yourself warily, but the lizard is nowhere in sight. You sigh in relief")
        score = (score + 1)
    else:
        print("That's not an option! The pink Lizard pounces on you, killing you insantly") 
        quit()
#Option 2= spear, gives all the options for if player picks 'spear'

elif answer == "tunnel":
    print("You quickly back into the tunnel you came from, hoping the lizard didnt notice you(it did)")
    time.sleep(3)
    print("you jump out the tunnel but hear an unfortunate noise behind you")
    def check():
        time.sleep(5)
        if tunnel != None:
            return
        print("You panic, taking too long to respond. The Pink Lizard snarls and pounces on you. Killing you.")
        quit()
    Thread(target = check).start()
    tunnel = input("Quick! What do you do?!RUN(turn and sprint away!) or play DEAD(maybe it wont eat you?)").lower()

    if tunnel == "dead":
        print("The lizard jumps out of the tunnel, ready to give chase!")
        time.sleep(2)
        print("It pauses before slowly looking down at you")
        time.sleep(2)
        print("Only a moment later, the Lizards jaws chomp down on you. It was gonna kill you anyway, why did you think that would work?")
        time.sleep(3)
        quit()
    elif tunnel == "run":
        print("You zip off! Not even looking back at the Lizard behind you as you jump and dive between the obsticles in your way. Finally you dive into a tunnel leading into another room.")
        time.sleep(2)
        print(" ")
        time.sleep(2)
        print("you look behind yourself warily, but the lizard is nowhere in sight. You sigh in relief")
#Option 3= tunel, gives all the options for if player picks 'tunnel'


else:
    print("That's not an option! The pink Lizard pounces on you, killing you insantly") 
    quit()
#for if player picks an option which is not 'rock', 'spear' or 'tunnel'

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
berry = False
#setting up the new room, giving player option of 'tunnel' or 'berries'

amount = 0
while roomchoice == False:
    if room == "berry" or room == "berries":
        print("You walk up to the berries, there are three of them")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        amount = 0
        
        while True:
            try:
                amount = int(input("How many do you eat? "))
                if amount >= 1 and amount <= 3:
                    break
                else:
                    print("Choose a number between 1&3")
            except ValueError:
                print("that's not an amount")
       
        while berry == False:
            if amount >= 1 or amount <= 3:
                roomchoice = True
                berry = True
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("After eating your fill of the berries, you walk towards the tunnel, curious of what's on the other side.")
#if player picks to go to berries

#3/13/25, 12:51, not working as intended, will crash when a number is not shown, will repeat when there is a number.
#attempting to make it so user needs to put a number and it saves as an int and moves on, but if they put something else, it will tell you you need to put a number
#18/03/25 9:10, fixed the repeating, the error is still there
#18/03/25 9:43, everything is fixed..... i think.... Thank you Whaea Munireh, The GOAT


            
    elif room == "room" or room == "tunnel":
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("You ignore the berries, deciding to walk through the tunnel, curious of what's on the other side.")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        roomchoice = True
    else:
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("that is not an option.")
        time.sleep(0.5)
        print(" ")
        time.sleep(0.5)
        room = input("what do you go to? ").lower()
#if player picks to go to room, will ignore berries and go to next code, if picks none of the above, the code will tell you its not an option and repeat input.

print("you warily peak out of the tunnel")
time.sleep(1)
print(" ")
time.sleep(1)
print("after checking there is no enemies, you properly walk in")
time.sleep(2)
print(" ")
time.sleep(2)
print("There is a shelter! if you ate enough food you can now sleep!")
choice2 = input("Do you go into the shelter or back into the other room?").lower()
#set up new room and the players options.
choice3 = False
if choice2 == "back" or choice2 == "go back" or choice2 == "tunnel" or choice2 == "room" or choice2 == "other room":
    roomberry(room)
    roomshelter()
    choice3 = True
#calling functions to repeat so players can get choice to go back once and get berries.

if choice2 == "shelter" or choice2 == "sleep" or choice3 == True:
    time.sleep(1)
    print(" ")
    time.sleep(1)
    print("you walk into the shelter, relieved to finally be safe")
    if amount < 3:
        print("you curl up into the shelter, trying to ignore your hunger.")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("the shelter closes behind you, but you feel something off as you fall asleep hungry")
        time.sleep(1)
        print(" ")
        time.sleep(2)
        print("--Cycle over. You got to a shelter but did not save, you starved.--")
    else:
        print("you curl up into the shelter")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("you sigh in relief as the shelter closes behind you, falling asleep")
        time.sleep(1)
        print(" ")
        time.sleep(2)
        print("--Cycle over. You got to a shelter and saved! You survived.--")
        score = (score + 2)
#game ending. if didnt get enough food(berries), then they starve, but still save. if got enough food, they save properly{best ending}

time.sleep(1)
print(" ")
time.sleep(2)
print(f"score = {score}")
time.sleep(1)
print(" ")
time.sleep(2)
exit()
#give score, then end.

