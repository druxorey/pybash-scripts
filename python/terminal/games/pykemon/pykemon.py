from colorama import Fore, Style
from visuals import *
import readchar
import os
import random

# Constants for position indexes
POS_X = 0
POS_Y = 1

# Constants for the game visual
RESET = f"{Style.RESET_ALL}"
LIMIT = f"{RESET}███"
WALL = f"{Fore.RED}███"

# Initial values
character_position = [8,10]
debug_mode = False

# Initial battle values
TRAINER = []
trainer_list = TRAINER
pokemon_list = ["pikachu", "squirtle", "charmander", "bulbasaur"]
initial_data = [pokemon_list[0]]

# Import map layout from the variable in the 'visuals.py' file
map_definition = MAP_LAYOUT

# Create obstacle map and initialize trainers
map_definition = [list(row) for row in map_definition.split("\n")]
trainer_id = 1
for coordinate_y in range(len(map_definition)):
    for coordinate_x in range(len(map_definition[0])):
        if map_definition[coordinate_y][coordinate_x] == "@":
            trainer_list.append([coordinate_x, coordinate_y, trainer_id])
            trainer_id += 1
            map_definition[coordinate_y][coordinate_x] = " "

# Constants for map dimensions
MAP_WIDTH = len(map_definition[0])
MAP_HEIGHT = len(map_definition)

# Show the screen with the tutorial
# os.system("clear")
# input(INTRODUCTION)

# Main game loop
while True:
    os.system("clear")
    trainer_combat = None

    print((LIMIT * MAP_WIDTH) + (LIMIT * 2))
    for coordinate_y in range(MAP_HEIGHT):
        print(LIMIT, end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "   "
            char_in_cell = None
            
            if map_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = WALL

            for char_in_cell in trainer_list:
                if char_in_cell[POS_X] == coordinate_x and char_in_cell[POS_Y] == coordinate_y:
                    char_to_draw = f"{RESET} 󰐝 "
                if character_position[POS_X] == coordinate_x and character_position[POS_Y] == coordinate_y:
                    char_to_draw = f"{RESET}  "
                    if char_in_cell[POS_X] == character_position[POS_X] and char_in_cell[POS_Y] == character_position[POS_Y]:
                        trainer_combat = char_in_cell[2]
                        break

            print(f"{char_to_draw}", end="")
        print(LIMIT)
    print((LIMIT * MAP_WIDTH) + (LIMIT * 2) + f"\n")

    # Debug mode
    if debug_mode == True:
        print("character_position: ",character_position)
        print("trainer_combat: ",trainer_combat)
        print("MAP_WIDTH",MAP_WIDTH)

    # Check if you are on a trainer to ask if you want to fight him
    if trainer_combat is not None:
        
        print("╔══" + ("═══" * MAP_WIDTH) + "══╗")
        print("║  " + (f"¿Empezar combate contra entrenador Nvl {trainer_combat}? [ENTER]").center(MAP_WIDTH * 3) + "  ║")
        print("╚══" + ("═══" * MAP_WIDTH) + "══╝")

    # Calculate the next position based on the input direction
    # Note: Uppercase letters are how the unix keyboard defines the keys, I discovered it by mistake and I'll leave it like that
    direction = readchar.readchar()
    next_position = character_position.copy()
    if direction in ["w", "A"]:
        next_position[POS_Y] -= 1
    elif direction in ["s", "B"]:
        next_position[POS_Y] += 1
    elif direction in ["a", "D"]:
        next_position[POS_X] -= 1
    elif direction in ["d", "C"]:
        next_position[POS_X] += 1
    elif direction in ["q", "Q"]:
        exit()
    elif direction == "b":
        debug_mode = not debug_mode
        continue
    elif direction == "\n":    
        if trainer_combat is not None:

            if trainer_combat == 3:
                pokimon = "CHARIZXDWADWA"
            elif trainer_combat == 2:
                input("Si funciona")
            elif trainer_combat == 1:
                input("Si funciona")

            os.system("clear")

            input(f"Empieza el combate de {pokimon}")
            
    # Check if the next position is a wall
    if map_definition[next_position[POS_Y]][next_position[POS_X]] != "#":
        character_position = next_position
