import readchar
import os
import random
from colorama import Fore, Style

# Constants for position indexes
POS_X = 0
POS_Y = 1

# Color variables
COLOR_CHARACTER = (Fore.YELLOW)
COLOR_RIVAL = (Fore.WHITE)
COLOR_RESET = (Style.RESET_ALL)
IN_WALL = f"{Fore.RED}███"
EX_WALL = f"{Style.RESET_ALL}███"

# Debug mode initial value
debug_mode = False

# Initial character values
character_position = [7,13]

# Initial objects values
object_main_list = []
map_objects = object_main_list

# Initial game values
level = 0
score = 0

# Map
obstacle_definition = """\
###############
#     ####   ##
# ##  #### @ ##
#@##         ##
####         ##
####  #########
#     #########
#     ##      #
#  #####      #
#  #########  #
#             #
#      @      #
######   ######
######   ######
######   ######
###############\
"""

# Create obstacle map and initialize rivals
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
RIVAL_ID = 1
for y in range(len(obstacle_definition)):
    for x in range(len(obstacle_definition[0])):
        if obstacle_definition[y][x] == "@":
            object_main_list.append([x, y, RIVAL_ID])
            RIVAL_ID += 1
            obstacle_definition[y][x] = " "

# Constants for map dimensions
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Main game loop
while True:

    os.system("clear")
    show_rival = None
    
    print((EX_WALL * MAP_WIDTH) + (EX_WALL * 2))
    for coordinate_y in range(MAP_HEIGHT):
        print(EX_WALL, end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "   "
            object_in_cell = None

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = IN_WALL
            for object_in_cell in map_objects:
                if object_in_cell[POS_X] == coordinate_x and object_in_cell[POS_Y] == coordinate_y:
                    char_to_draw = f"{COLOR_RIVAL} 󰐝 "
            if character_position[POS_X] == coordinate_x and character_position[POS_Y] == coordinate_y:
                char_to_draw = f"{COLOR_CHARACTER}  "

                for object_in_cell in map_objects:
                    if object_in_cell[POS_X] == character_position[POS_X] and object_in_cell[POS_Y] == character_position[POS_Y]:
                        show_rival = object_in_cell[2]
                        break
            print(f"{char_to_draw}", end="")
        print(EX_WALL)
    print((EX_WALL * MAP_WIDTH) + (EX_WALL * 2) + f"\n")
    
    if show_rival is not None:
        if show_rival == 3:
            menu_pos = 0
            menu_height = 2
            
            print((EX_WALL * MAP_WIDTH) + (EX_WALL * 2))
            for attack in range(menu_height):

                print(EX_WALL, end="")
                if attack == menu_pos:
                    print(("►" + "dinosaurio" + "◄").center(MAP_WIDTH * 3), end="")
                else:
                    print(("option").center(MAP_WIDTH * 3), end="")
                print(EX_WALL)
            print((EX_WALL * MAP_WIDTH) + (EX_WALL * 2))

            menu_selector = readchar.readkey()

            if menu_selector == "w":
                menu_pos -= 1
                menu_pos %= menu_height
            elif menu_selector == "s":
                menu_pos += 1
                menu_pos %= menu_height
            elif menu_selector == "g":
                step = 2
            elif menu_selector == "q":
                break
        # defeated = input(f"¿Deseas eliminar al rival {show_rival}? (S/N): ")
        # if defeated.lower() == "s":
        #     map_objects = [object_in_cell for object_in_cell in map_objects if object_in_cell[2] != show_rival]

    # Debug mode
    if debug_mode == True:
        print("Ubicación de los objetos del mapa: ",map_objects)
        print("Objetos del mapa: ",len(map_objects))
        print("Posición del personaje: ",character_position)

    # Read the next direction from the user
    direction = readchar.readchar()

    # Calculate the next position based on the input direction
    next_position = character_position.copy()
    #* Note: Uppercase letters are how the unix keyboard defines the keys, I discovered it by mistake and I'll leave it like that
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

    # Check if the next position is a wall
    if obstacle_definition[next_position[POS_Y]][next_position[POS_X]] != "#":
        character_position = next_position
    else:
        continue
