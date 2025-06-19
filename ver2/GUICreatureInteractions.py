# imports and set ups
import time
import random
import sys
import winsound
import threading
import defs as d


d.call_all_defs()


d.ImageLabel(bg="#180821")
"""




"""
if d.has_spear is False:
    scav_scug=d.ImageLabel(d.app, borderwidth=0)
    scav_scug.pack(padx=10, pady=10)
    scav_scug.load('scavandscug.gif')
    scav_scug.place(x=0, y=0)
else:
    scav_scugsp=d.ImageLabel(d.app, borderwidth=0)
    scav_scugsp.pack(padx=10, pady=10)
    scav_scugsp.load('scavandscugspear.gif')
    scav_scugsp.place(x=0, y=0)

scav_dodge_run=d.ImageLabel(d.app, borderwidth=0)
scav_dodge_run.pack(padx=10, pady=10)
scav_dodge_run.place(x=0, y=0)

spike=d.ImageLabel(d.app, borderwidth=0)
spike.pack(padx=10, pady=10)
spike.place(x=0, y=0)

spiked=d.ImageLabel(d.app, borderwidth=0)
spiked.pack(padx=10, pady=10)
spiked.place(x=0, y=0)

scav_miss=d.ImageLabel(d.app, borderwidth=0)
scav_miss.pack(padx=10, pady=10)
scav_miss.place(x=0, y=0)

scug=d.ImageLabel(d.app, borderwidth=0)
scug.pack(padx=10, pady=10)
scug.place(x=0, y=0)

scav_kill=d.ImageLabel(d.app, borderwidth=0)
scav_kill.pack(padx=10, pady=10)
scav_kill.place(x=0, y=0)

scug_run_crouch=d.ImageLabel(d.app, borderwidth=0)
scug_run_crouch.pack(padx=10, pady=10)
scug_run_crouch.place(x=0, y=0)

crouch=d.ImageLabel(d.app, borderwidth=0)
crouch.pack(padx=10, pady=10)
crouch.place(x=0, y=0)

scav_killed=d.ImageLabel(d.app, borderwidth=0)
scav_killed.pack(padx=10, pady=10)
scav_killed.place(x=0, y=0)

cscav_kill=d.ImageLabel(d.app, borderwidth=0)
cscav_kill.pack(padx=10, pady=10)
cscav_kill.place(x=0, y=0)

c_scav_run=d.ImageLabel(d.app, borderwidth=0)
c_scav_run.pack(padx=10, pady=10)
c_scav_run.place(x=0, y=0)


end_screen=d.ImageLabel(d.app, borderwidth=0)
end_screen.pack(padx=10, pady=10)                 
end_screen.place(x=0, y=0)
# Code in order to set up the gifs to work later
# would like to find out how to make the gif change, instead of making a new one each time.

def scav_gui():
    """This code will simulate an encounter between the user and a creature Known as a Scavenger.

    This function initiates an encounter between the player and a creature known as a Scavenger, with
    outcomes which are influenced by both the players actions, available weaponry they have aswell as rng.
    The interaction includes paths the user can chose, including aggressive, peaceful and cowardly,
    each having their own consequences.

    The function handles:
        -Plays threat music as the rest of the code plays out.
        -Displays narrative text which describes what is happening based both on player reputation and their actions.
        -Manages Player actions such as attacking with a spear, dropping the spear, crouching or running away.
        -Triggers different outcomes based on random chance(RNG) and predefined conditions.

    secondary effects:
        -Modifies the global Variables such as 'runaway' and 'has_spear' based on user actions and encounter outcomes.
        -Modifies the Reputation Function by adding to the 'aggression' Variable.

    Notes:
        -The encounter is largely influenced by the users actions aswell as their previously established 'reputation'.
        -The way the user acted during this encounter will affect their future interactions with any other scavenger.
    """
    winsound.PlaySound('threat.wav', winsound.SND_ASYNC)
    # winsound!!!! will play the audio as the gameplays and will loop!
    # playing any other sound cancels this but i am gonna attempt to fix this :3
    # I HAVE PERMISSION FROM RIVOTTER AND JAMES THERRIAN(James Primate)
    # TO USE BOTH THE MUSIC AND AUDIO FROM THE GAME: Rain World by Video Cult
    text = ("You look towards the creature in front of you, it looks back at you.\n It's quills spike up.")
    d.print_string(text)
    if d.reputation(d.aggression) <= 1:
        text = ("The Scavenger looks at you warily, clutching it's spear to\nit's chest protectively  ")
        d.print_string(text)
    elif d.reputation(d.aggression) > 1 and d.reputation(d.aggression) <= 3:
        text = ("The Scavenger raises it's spear towards you, but seems more\ndefensive than offensive")
        d.print_string(text)
    else:
        text = ("The Scavenger frills up, raising it's spear, and you know\nit intends to use it.")
        d.print_string(text)
    # if, elif, else statements depending on the players reputation with the scavenger and changing the starting statement.
    if d.has_spear is True:
        text = ("You look warily at the Scavenger, raising your own Spear defensively")
        d.print_string(text)
        text = ("You think of your options. Throw the Spear at it?\nDrop the weapon for peace??")
        d.print_string(text)
        action = input("What do you do? ").lower()
        if action == "throw" or action == "throw spear" or action == "attack":
            d.aggression += 3
            d.has_spear = False
            if d.attack_chance() >= 2:
                # scug misses
                if d.reputation_rng() < 0:
                    # scav run
                    scav_dodge_run.load('scav_dodge_run.gif')
                    text = ("The scavenger jumps out of the way, scrambling to it's feet and staring at you")
                    d.print_string(text)
                    text = ("Without another thought the scavenger dives towards a tunnel, squeezing through and running away")
                    d.print_string(text)
                    scav_scugsp.load('scug.gif')
                    runaway = True
                elif d.reputation_rng() > 0:
                    # scav angry
                    spike.load('spikeup.gif')
                    text = ("The scavenger jumps out of the way, scrambling to it's feet and staring at you")
                    d.print_string(text)
                    spiked.load('spikedup.gif')
                    spike.configure(image=None)
                    text = ("It raises it's spear to you")
                    d.print_string(text)
                    if d.attack_chance() >= 2:
                        # scav misses
                        text = ("...")
                        d.print_string(text)
                        scav_miss.load('scav_miss.gif')
                        text = ("The spear clanks to the ground next to you")
                        d.print_string(text)
                        text = ("O_O'")
                        scug.load('scug.gif')
                        d.print_string(text)
                        text = ("The Scavenger sprints in to the tunnel next to it")
                        d.print_string(text)
                    else:
                        # scav hits
                        text = ("...")
                        d.print_string(text)
                        scav_miss.load('scavhit.gif')
                        text = ("The spear stabs right through your chest.")
                        d.print_string(text)
                        text = ("The last thing you see before your vision goes black \n is the Scavenger running off")
                        d.print_string(text)
                        end_screen.load('black.gif')
                        text = ("YOU DIED")
                        d.print_string(text)
                        winsound.PlaySound('death.wav', winsound.SND_FILENAME)
                        d.sleepy()
                        d.app.destroy()
                        quit
                else:
                    text = ("what,,,,,")
                    d.print_string(text)
                    exit()
            else:
                text = ("The spear peirces the Scavengers chest")
                d.print_string(text)
                scav_killed.load('scavstabbed.gif')
                text = ("The creature doesn't even get a chance to react")
                d.print_string(text)
                d.app.destroy()
                quit
        elif action == "drop" or action == "drop spear" or action == "peace":
            d.has_spear = False
            d.aggression -= 2
            text = ("You slowly toss the spear away from yourself")
            d.print_string(text)
            end_screen.load('scavandscug.gif')
            text = ("The scavenger blinks at you, lowering it's own spear")
            d.print_string(text)
            text = ("you look at one another for a second before the scavenger runs off")
            d.app.destroy()
            quit
        else:
            text = ("you didnt know what to do\njust standing there like an idiot")
            d.print_string(text)
            text = ("The scavenger raises it's spear at you nervously")
            if d.attack_chance() > 2:
                text = ("...")
                d.print_string(text)
                scav_miss.load('scav_miss.gif')
                text = ("The spear clanks to the ground next to you")
                d.print_string(text)
                text = ("O_O'")
                d.print_string(text)
                text = ("The Scavenger sprints in to the tunnel next to it")
                d.print_string(text)
                print('next room')
            else:
                text = ("...")
                d.print_string(text)
                scav_miss.load('scavhit.gif')
                text = ("The spear stabs right through your chest.")
                d.print_string(text)
                text = ("The last thing you see before your vision goes black \n is the Scavenger running off")
                d.print_string(text)
                end_screen.load('black.gif')
                text = ("YOU DIED")
                d.print_string(text)
                winsound.PlaySound('death.wav', winsound.SND_FILENAME)
                d.sleepy()
                d.app.destroy()
                quit

    else:
        text = ("You look warily at the Scavenger, seeing it's armed with a spear")
        d.print_string(text)
        text = ("you think of your options. Try to run past? maybe crouch to show you aren't a threat")
        d.print_string(text)
        action = input("What do you do? ").lower()
        if action == "run" or action == "run past":
            d.aggression += 1
            text = ("You just decide to sprint past the Scavenger...")
            d.print_string(text)
            scug_run_crouch.load("scugrun.gif")
            text = ("........")
            d.print_string(text)
            d.app.destroy()
            quit
        elif action == "crouch" or action == "crouch down":
            d.aggression -= 2
            text = ("You crouch down in front of the scavenger")
            d.print_string(text)
            scug_run_crouch.load("crouch.gif")
            d.sleepy()
            d.sleepy()
            crouch.load("crouching.gif")
            if d.reputation(d.aggression) <= 1:
                text = ("The scavenger blinks at you, it looks quite curious")
                d.print_string(text)
                c_scav_run.load('crouchscavrun.gif')
                text = ("it turns away and runs off")
                d.print_string(text)
                d.app.destroy()
                quit
            elif d.reputation(d.aggression) > 1 and d.reputation(d.aggression) <= 3:
                text = ("The scavenger looks at you nervously")
                d.print_string(text)
                c_scav_run.load('crouchscavrun.gif')
                text = ("it turns away and runs off")
                d.print_string(text)
                d.app.destroy()
                quit
            else:
                text = ("the scavenger raises it's spear, not at all phased by your gesture.")
                d.print_string(text)
                cscav_kill.load('crouchscavhit.gif')
                text = ("The spear stabs right through your chest.")
                d.print_string(text)
                end_screen.load('black.gif')
                text = ("YOU DIED")
                d.print_string(text)
                winsound.PlaySound('death.wav', winsound.SND_FILENAME)
                d.sleepy()
                d.app.destroy()
                quit
        else:
            text = ("you didnt know what to do\njust standing there like an idiot")
            d.print_string(text)
            text = ("The scavenger raises it's spear at you nervously")
            if d.attack_chance() > 2:
                text = ("...")
                d.print_string(text)
                scav_miss.load('scav_miss.gif')
                text = ("The spear clanks to the ground next to you")
                d.print_string(text)
                text = ("O_O'")
                d.print_string(text)
                text = ("The Scavenger sprints in to the tunnel next to it")
                d.print_string(text)
                d.app.destroy()
                quit
            else:
                text = ("...")
                d.print_string(text)
                scav_miss.load('scavhit.gif')
                text = ("The spear stabs right through your chest.")
                d.print_string(text)
                text = ("The last thing you see before your vision goes black \n is the Scavenger running off")
                d.print_string(text)
                end_screen.load('black.gif')
                text = ("YOU DIED")
                d.print_string(text)
                winsound.PlaySound('death.wav', winsound.SND_FILENAME)
                d.sleepy()
                d.app.destroy()
                quit

print(scav_gui())


app.mainloop()