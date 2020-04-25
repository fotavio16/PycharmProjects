'''
    Python Text RPG

'''

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player Setup #####
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []

myPlayer = player()

##### Title Screen #####
def title_screen_selections():
    option = ""
    while option.lower() not in ['play', 'help', 'quit']:
        option = input("> ")
        if option.lower() == ("play"):
            start_game() # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
        else:
            print("Please enter a valid command.")

def title_screen():
    os.system('cls')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print('     Copyright 2020 Fogf    ')
    title_screen_selections()

def help_menu():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    print('- Good luck and have fun!')
    title_screen_selections()


##### GAME FUNCTIONALITY #####
def start_game():
    title_screen()


##### MAP #####
'''
a1 a2... # PLAYER STARTS AT b2
---------
| | | | | a4
---------
| | | | | b4
---------
| | | | | c4
---------
| | | | | d4
---------
'''

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }

zonemap = {
    'a1': {
        ZONENAME: "Town Market",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "",
        DOWN: "b1",
        LEFT: "",
        RIGHT: "a2"
    },
    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "",
        DOWN: "b2",
        LEFT: "a1",
        RIGHT: "a3"
    },
    'a3': {
        ZONENAME: "Town Square",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "",
        DOWN: "b3",
        LEFT: "a2",
        RIGHT: "a4"
    },
    'a4': {
        ZONENAME: "Town Hall",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "",
        DOWN: "b4",
        LEFT: "a3",
        RIGHT: ""
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "a1",
        DOWN: "c1",
        LEFT: "",
        RIGHT: "b2"
    },
    'b2': {
        ZONENAME: "Home",
        DESCRIPTION: "This is your home!",
        EXAMINATION: "Your home looks the same - nothing has changed.",
        SOLVED: False,
        UP: "a2",
        DOWN: "c2",
        LEFT: "b1",
        RIGHT: "b3"
    },

}




start_game()


