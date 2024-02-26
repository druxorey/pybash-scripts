import readchar
import os
import random

# Constants for position indexes
POS_X = 0
POS_Y = 1

# Constants for map dimensions
MAP_WIDTH = 20
MAP_HEIGHT = 15

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
character_position = [10,7]
tail_length = 1
tail = []

# Initial objects values
object_quantity = random.randint(1,4)
object_main_list = []
map_objects = object_main_list

# Initial game values
level = 0
score = 0

# Main game loop
while True:

    os.system("clear")

    # generate random objects in the map
    if len(map_objects) <= 0:
        object_quantity += 1
        level += 1
        for _ in range(object_quantity):
            object_main_list.append([random.randint(0,(MAP_WIDTH - 1 )),random.randint(0,(MAP_HEIGHT - 1 ))])

    print("╔" + "═" * MAP_WIDTH * 3 + "╗")

    for coordinate_y in range(MAP_HEIGHT):
        print("║", end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None

            for map_object in map_objects:

                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "󰉛"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = ""

            if character_position[POS_X] == coordinate_x and character_position[POS_Y] == coordinate_y:
                char_to_draw = ""
                
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                    score += 1

            print(f" {char_to_draw} ", end="")
        
        print("║")

    print("╚" + "═" * MAP_WIDTH * 3 + "╝")

    # User data
    print(f"Nivel: {level}")
    print(f"Puntaje: {score}")
        
    # Debug mode
    if debug_mode == True:
        print("Ubicación de los objetos del mapa: ",map_objects)
        print("Objetos del mapa: ",len(map_objects))
        print("Posición del personaje: ",character_position)
        print("Largo de la cola: ",tail_length)

    # Read the next direction from the user
    direction = readchar.readchar()

    # Update the character position based on the input direction
    if direction == UP:
        character_position[POS_Y] -= 1
        if character_position[POS_Y] < 0:
            character_position[POS_Y] = (MAP_HEIGHT - 1)
    
    elif direction == DOWN:
        character_position[POS_Y] += 1
        if character_position[POS_Y] > (MAP_HEIGHT - 1):
            character_position[POS_Y] = (0)
    
    elif direction == LEFT:
        character_position[POS_X] -= 1
        if character_position[POS_X] < 0:
            character_position[POS_X] = (MAP_WIDTH - 1)
    
    elif direction == RIGHT:
        character_position[POS_X] += 1
        if character_position[POS_X] > (MAP_WIDTH - 1):
            character_position[POS_X] = (0)
    
    elif direction == QUIT:
        exit()
    
    elif direction == DEBUG:
        debug_mode = not debug_mode
        continue

    # Check if the character has collided with the tail
    for tail_piece in tail[1:]:  
        if tail_piece[POS_X] == character_position[POS_X] and tail_piece[POS_Y] == character_position[POS_Y]:
            os.system("clear")
            print("¡Has perdido!")
            print(f"Has llegado al nivel: {level}")
            print(f"Tu puntaje fue de: {score}")
            exit()

    # Update the tail position
    tail.insert(0,character_position.copy())
    tail = tail[:tail_length]
    
