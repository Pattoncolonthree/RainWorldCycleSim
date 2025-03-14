import time
from threading import Thread
seconds = time.time()
local_time = time.ctime(seconds)


room = input("what do you go to? ").lower()
roomchoice = False

while roomchoice == False:
    if room == "berry" or room == "berries":
        print("You walk up to the berries, there are three of them")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        amount = input("How many do you eat? ")
        roomchoice = True
    elif room == "room" or room == "tunnel":
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("You ignore the berries, deciding to walk through the tunnel, curious of what's on the other side.")
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
#3/13/25, 12:51, not working as intended, will crash when a number is not shown, will repeat when there is a number.
#attempting to make it so user needs to put a number and it saves as an int and moves on, but if they put something else, it will tell you you need to put a number

print("woah")
