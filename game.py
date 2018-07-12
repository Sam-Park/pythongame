# Python Text RPG
# Made by Sam Park
from gameObjects import *
import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### Player Setup ####
class player: 
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mana = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False
        self.job = ""

newPlayer = player()

###### Title Screen ######

def title_screen_selections():
    option = input(">> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input(">> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
def title_screen():
    os.system('clear')
    print("#############################")
    print("#  Welcome to the text RPG  #")
    print("#############################")
    print("#         -Play-            #")
    print("#         -Help-            #")
    print("#         -Quit-            #")
    print("#        Copyright lol      #")
    title_screen_selections()

def help_menu():
    print("#############################")
    print("#  Welcome to the text RPG  #")
    print("#############################")
    print("#   -use n,s,e,w to move-   #")
    print("# Use l or look to inpsect  #")
    title_screen_selections()





###### Game interactivity ####

def print_location():
    print('\n' + ("#" * (2 * len(zonemap[newPlayer.location][ZONENAME]))))
    print('# ' + zonemap[newPlayer.location][ZONENAME].upper() + ' #')
    print('# ' + zonemap[newPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ("#" * (2 * len(zonemap[newPlayer.location][ZONENAME]))))

def promt():
    print("\n" + "======================")
    action = input(">> ")
    acceptable_actions = ['n', 's', 'e', 'w', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.strip().lower() not in acceptable_actions:
        print('Unknown action, try again.\n' )
        action = input(">> ")
    if action.strip().lower() == 'quit':
        sys.exit()
    elif action.strip().lower() in ['n', 's', 'e', 'w', ]:
        if action == "n":
            action = Up
            player_move(action)
        elif action == "s":
            action = Down
            player_move(action)
        elif action == "w":
            action = Left
            player_move(action)
        elif action == "e":
            action = Right
            player_move(action)
    elif action.strip().lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.strip().lower())

def player_move(myAction):
    dest = myAction
    if dest not in zonemap[newPlayer.location]:
        print("You bump into the wall, try another exit")
    elif dest == Up:
        dest = 'n'
        if dest in ["n"]:
            destination = zonemap[newPlayer.location][Up]
            movement_handler(destination)
    elif dest == Down:
        dest = "s"
        if dest in ["s"]:
            destination = zonemap[newPlayer.location][Down]
            movement_handler(destination)
    elif dest == Right:
        dest = "e"
        if dest in ["e"]:
            destination = zonemap[newPlayer.location][Right]
            movement_handler(destination)
    elif dest == Left:
        dest = "w"
        if dest in ["w"]:
            destination = zonemap[newPlayer.location][Left]
            movement_handler(destination)

def movement_handler(destination):
    print("\n" + "You have moved to " + destination + ".")
    newPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap[newPlayer.location][SOLVED]:
        print("You have already exhausted this zone.")
    elif zonemap[newPlayer.location][room]: 
        print(rooms[newPlayer.location][DESCRIPTION])
        print(rooms[newPlayer.location][THINGS])
    else:
        print(zonemap[newPlayer.location][ZONENAME])
        print(zonemap[newPlayer.location][EXAMINATION])

   


##### Game functionality #########



def main_game_loop():
    while newPlayer.game_over is False:
        promt()
    #here handle if puzzles have been solved, boss defeated, explored everything


def setup_game():
    os.system('clear')

    #### Name Collecting
#    question1 = "Hello, what's your name?\n"
#    for character in question1:
#        sys.stdout.write(character)
#        sys.stdout.flush()
#        time.sleep(0.05)
#    player_name = input(">> ")
#    newPlayer.name = player_name
#    
#    ##### Job Handling ####
#    question2 = "What, class are you?\n"
#    question2added = "(You can play as a warrior, priest or a mage)\n"
#    for character in question2:
#        sys.stdout.write(character)
#        sys.stdout.flush()
#        time.sleep(0.05)
#    for character in question2added:
#        sys.stdout.write(character)
#        sys.stdout.flush()
#        time.sleep(0.01)
#    player_job = input(">> ")
#    valid_jobs = ["warrior", 'mage', 'priest']
#    if player_job.strip().lower() in valid_jobs:
#        newPlayer.job = player_job
#        print("You are now a " + player_job + " !\n")
#    while player_job.strip().lower() not in valid_jobs:
#        player_job = input(">> ")
#        if player_job.strip().lower() in valid_jobs: 
#            newPlayer.job = player_job
#            print("You are now a " + player_job + " !\n")

    ##### player stats ######
 #   if newPlayer.job is 'warrior':
 #       self.hp = 120
 #       self.mana = 30
 #   elif newPlayer.job is 'mage':
 #       self.hp = 90
 #       self.mana = 65
 #   elif newPlayer.job is 'priest':
 #       self.hp = 105
 #       self.mana = 50

#### INTRODUCTION #########
#    question3 = "Welcome, " + newPlayer.name + " the " + newPlayer.job +".\n"
#    for character in question3:
#        sys.stdout.write(character)
#        sys.stdout.flush()
#        time.sleep(0.05)


#    speech1 = "Welcome to the world\n"
#    speech2 = "Good luck, dont die\n"
#    speech3 = "Just kidding, I hope a spider bites you and then you die\n"
#    speech4 = "heheheheh........\n"
#    for character in speech1:
#            sys.stdout.write(character)
#            sys.stdout.flush()
#            time.sleep(0.03)
#    for character in speech2:
#            sys.stdout.write(character)
#            sys.stdout.flush()
#            time.sleep(0.03)
#    for character in speech3:
#            sys.stdout.write(character)
#            sys.stdout.flush()
#            time.sleep(0.05)
#    for character in speech4:
#            sys.stdout.write(character)
#            sys.stdout.flush()
#            time.sleep(0.2)

    os.system('clear')
    print("#######################")
    print("#   Let's start now!  #")
    print("#######################")
    main_game_loop()

title_screen()