# Python Text RPG
# Made by Sam Park

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

##### game functionality ####





ZONENAME = ""
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
Up = "up", "north", "n"
Down = "down", "south", "s"
Left = "left", "east", "e"
Right = "right", "west", "w"

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False,
                }

zonemap = {
    'a1': {
        ZONENAME: "Town Market",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: "",
        Down: "b1",
        Left: "",
        Right: "a2",
    },
    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION:'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: "",
        Down: "b2",
        Left: "a1",
        Right: "a3",
    },
    'a3': {
        ZONENAME: "Town Square",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: "",
        Down: "b3",
        Left: "a2",
        Right: "a4",
    },
    'a4': {
        ZONENAME: "Town Hall",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: "",
        Down: "b4",
        Left: "a3",
        Right: "",
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: "a1",
        Down: "c1",
        Left: "",
        Right: "b2",
    },
    'b2': {
        ZONENAME: "Home",
        DESCRIPTION: 'This is your Home!',
        EXAMINATION: "It hasn't changed since the last time you looked...",
        SOLVED: False,
        Up: "a2",
        Down: "c2",
        Left: "b1",
        Right: "b3",
    },
    'b3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: "a3",
        Down: "c3",
        Left: "b2",
        Right:"b4",
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: "a4",
        Down: "c4",
        Left: "b3",
        Right: "",
    },
}

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
        player_move(action.strip().lower())
    elif action.strip().lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.strip().lower())

def player_move(myAction):
    dest = myAction
    if dest not in zonemap[newPlayer.location]:
        print("You bump into the wall, try another exit")
    elif dest in ["n", "north"]:
        destination = zonemap[newPlayer.location][Up]
        movement_handler(destination)
    elif dest in ["s", "south"]:
        destination = zonemap[newPlayer.location][Down]
        movement_handler(destination)
    elif dest in ["e", "east"]:
        destination = zonemap[newPlayer.location][Left]
        movement_handler(destination)
    elif dest in ["w", "west"]:
        destination = zonemap[newPlayer.location][Right]
        movement_handler(destination)

def movement_handler(destination):
    print("\n" + "You have moved to " + destination + ".")
    newPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap[newPlayer.location][SOLVED]:
        print("You have already exhausted this zone.")
    else:
        print_location()


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