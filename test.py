room = input("what do you go to? ").lower()
berry = False
roomchoice = False
import time
from threading import Thread
seconds = time.time()
local_time = time.ctime(seconds)

while roomchoice == False:
    if room == "berry" or room == "berries":
        print("You walk up to the berries, there are three of them")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        amount=0
        
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
#3/13/25, 12:51, not working as intended, will crash when a number is not shown, will repeat when there is a number.
#attempting to make it so user needs to put a number and it saves as an int and moves on, but if they put something else, it will tell you you need to put a number
#18/03/25, fixed the repeating, the error is still there

print("woah")
