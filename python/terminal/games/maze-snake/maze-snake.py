import readchar
import os
import random
from visuals import *
from colorama import Fore, Style

# Constants for position indexes
POS_X = 0
POS_Y = 1

# Color variables
COLOR_CHARACTER = (Fore.YELLOW)
COLOR_APPLE = (Fore.RED)
COLOR_POTION = (Fore.GREEN)
COLOR_WALL = (Fore.BLUE)
COLOR_RESET = (Style.RESET_ALL)

# Debug mode initial value
debug_mode = False

# Constants for movement directions
UP = "w"
DOWN = "s"
LEFT = "a"
RIGHT = "d"
QUIT = "q"
DEBUG = "b"

# Initial character values
character_position = [12,12]
tail_length = 1
tail = []

# Initial apples values
apple_quantity = random.randint(4,8)
apple_main_list = []
map_apples = apple_main_list

# Initial potions values
potion_quantity = random.randint(1,3)
potion_main_list = []
map_potions = potion_main_list

# Initial game values
level = 0
score = 0
 
# Create obstacle map
aleatory_map = random.randint(1,2)

if aleatory_map == 1:
    obstacle_definition = first_map

elif aleatory_map == 2:
    obstacle_definition = second_map

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

# Constants for map dimensions
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Game start tutorial
os.system("clear")
print(tutorial_screen)
input("")

# Main game loop
while True:

    os.system("clear")

    # generate random apples in the map
    if len(map_apples) <= 0:
        apple_quantity += 1
        level += 1
        for _ in range(apple_quantity):
            while True:
                new_apple_position = [random.randint(0,(MAP_WIDTH - 1 )),random.randint(0,(MAP_HEIGHT - 1 ))]
                # Check if the new position is a wall
                if obstacle_definition[new_apple_position[POS_Y]][new_apple_position[POS_X]] != "#":
                    apple_main_list.append(new_apple_position)
                    break
        # generate random potions in the map
        if len(map_potions) <= 0:
            potion_quantity += 1
            for _ in range(potion_quantity):
                while True:
                    new_potion_position = [random.randint(0,(MAP_WIDTH - 1 )),random.randint(0,(MAP_HEIGHT - 1 ))]
                    # Check if the new position is a wall
                    if obstacle_definition[new_potion_position[POS_Y]][new_potion_position[POS_X]] != "#":
                        potion_main_list.append(new_potion_position)
                        break

    print(f"{COLOR_RESET}███" + "███" * MAP_WIDTH  + "███")
    for coordinate_y in range(MAP_HEIGHT):
        print("███", end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "   "
            apple_in_cell = None
            potion_in_cell = None

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = f"{COLOR_WALL}███"

            for map_apple in map_apples:

                if map_apple[POS_X] == coordinate_x and map_apple[POS_Y] == coordinate_y:
                    char_to_draw = f"{COLOR_APPLE} 󰉛 "
                    apple_in_cell = map_apple
            
            for map_potion in map_potions:

                if map_potion[POS_X] == coordinate_x and map_potion[POS_Y] == coordinate_y:
                    char_to_draw = f"{COLOR_POTION}  "
                    potion_in_cell = map_potion

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = f"{COLOR_CHARACTER}  "

            if character_position[POS_X] == coordinate_x and character_position[POS_Y] == coordinate_y:
                char_to_draw = f"{COLOR_CHARACTER}  "
                
                if apple_in_cell:
                    map_apples.remove(apple_in_cell)
                    tail_length += 1
                    score += 1

                if potion_in_cell:
                    map_potions.remove(potion_in_cell)
                    tail_length -= 1
                    score += 5

            print(f"{char_to_draw}", end="")
        
        print(f"{COLOR_RESET}███")

    print("███" + "███" * MAP_WIDTH  + "███")
    print(f"\n")

    # User data
    level_message = f"   Nivel: {str(level).zfill(2)}   "
    score_message = f"Puntuación: {str(score).zfill(3)}"

    data_length = int((len(level_message) + len(score_message)) / 4)
    data_visual = ("   " * (int(MAP_WIDTH / 2) - int(data_length / 2))) 

    print("███" + "███" * MAP_WIDTH  + "███")
    print("███" + data_visual + "   " + score_message + "   " + data_visual + "███")
    print("███" + data_visual + "   " + level_message + "   " + data_visual + "███")
    print("███" + "███" * MAP_WIDTH  + "███")

    # Debug mode
    if debug_mode == True:
        print("Ubicación de las manzanas del mapa: ",map_apples)
        print("Ubicación de las pociones del mapa: ",map_potions)
        print("Objetos del mapa: ",len(map_apples) + len(map_potions))
        print("Posición del personaje: ",character_position)
        print("Largo de la cola: ",tail_length)

    # Read the next direction from the user
    direction = readchar.readchar()

    # Calculate the next position based on the input direction
    next_position = character_position.copy()
    if direction == UP:
        next_position[POS_Y] -= 1
        if next_position[POS_Y] < 0:
            next_position[POS_Y] = (MAP_HEIGHT - 1)

    elif direction == DOWN:
        next_position[POS_Y] += 1
        if next_position[POS_Y] > (MAP_HEIGHT - 1):
            next_position[POS_Y] = (0)

    elif direction == LEFT:
        next_position[POS_X] -= 1
        if next_position[POS_X] < 0:
            next_position[POS_X] = (MAP_WIDTH - 1)

    elif direction == RIGHT:
        next_position[POS_X] += 1
        if next_position[POS_X] > (MAP_WIDTH - 1):
            next_position[POS_X] = (0)

    elif direction == QUIT:
        exit()

    elif direction == DEBUG:
        debug_mode = not debug_mode
        continue

    # Check if the next position is a wall
    if obstacle_definition[next_position[POS_Y]][next_position[POS_X]] != "#":
        character_position = next_position
    else:
        continue
    
    # Check if the character has collided with the tail
    for tail_piece in tail[1:]:  
        if tail_piece[POS_X] == character_position[POS_X] and tail_piece[POS_Y] == character_position[POS_Y]:
            os.system("clear")
            print("GAME OVER")
            print(f"Tu puntuación final: {score}")
            print(f"Has llegado al nivel: {level}")
            exit()

    # Update the tail position
    tail.insert(0,character_position.copy())
    tail = tail[:tail_length]
