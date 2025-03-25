import time

def roomberry(room):
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
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("After eating your fill of the berries, you walk towards the tunnel, curious of what's on the other side.")
            
            
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




def roomshelter():
    print("you warily peak out of the tunnel")
    time.sleep(1)
    print(" ")
    time.sleep(1)
    print("after checking there is no enemies, you walk towards the shelter")
    time.sleep(2)
    print(" ")
    time.sleep(2)
    choice3 = True