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
HEART = Fore.RED
WALL = f"{Fore.RED}███"

# Initial values
character_position = [8,10]
debug_mode = False

# Initial battle values
trainer_list = []
pokemon_list = ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"]
pokemon_life = [60, 70, 80, 90]

pikachu_attack = ["Placaje", "Chispa", "Trueno"]
pikachu_data = [pokemon_list[0], pokemon_life[0]]

squirtle_attack = ["Placaje", "Pistola Agua"]
squirtle_data = [pokemon_list[1], pokemon_life[1]]

charmander_attack = ["Placaje", "Ascuas"]
charmander_data = [pokemon_list[2], pokemon_life[2]]

bulbasaur_attack = ["Placaje", "Latigo Cepa"]
bulbasaur_data = [pokemon_list[3], pokemon_life[3]]

# Import map layout from the variable in the 'visuals.py' file
map_definition = MAP_LAYOUT

# Create obstacle map and initialize trainers
map_definition = [list(row) for row in map_definition.split("\n")]
trainer_id = 3
for coordinate_y in range(len(map_definition)):
    for coordinate_x in range(len(map_definition[0])):
        if map_definition[coordinate_y][coordinate_x] == "@":
            trainer_list.append([coordinate_x, coordinate_y, trainer_id])
            trainer_id -= 1
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
        print("trainer_combat: ",trainer_list)
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
                trainer_pokemon = [bulbasaur_data[0], bulbasaur_data[1]]
            elif trainer_combat == 2:
                trainer_pokemon = [charmander_data[0], charmander_data[1]]
            elif trainer_combat == 1:
                trainer_pokemon = [squirtle_data[0], squirtle_data[1]] 

            player_life = pikachu_data[1]
            trainer_life = trainer_pokemon[1]
            message = f"Entrenador saca a {trainer_pokemon[0]}"

            end_combat = None
            while end_combat != True:
                os.system("clear")

                life_center = int((MAP_WIDTH*3)/2)

                display_player_life = f"{pikachu_data[0]} Ps.{player_life}/{pikachu_data[1]}"
                display_trainer_life = f"{trainer_pokemon[0]} Ps.{trainer_life}/{trainer_pokemon[1]}"

                display_player_hearts = " " * (int(player_life / pikachu_data[1] * 10)) 
                display_trainer_hearts = " " * (int(trainer_life / trainer_pokemon[1] * 10)) 

                print("╔══" + ("═══" * MAP_WIDTH) + "══╗")
                print("║  " + message.center(MAP_WIDTH * 3) + "  ║")
                print("╚══" + ("═══" * MAP_WIDTH) + "══╝")

                print("╔══" + ("═══" * MAP_WIDTH) + "══╗")
                print("║  " + (display_player_life).ljust(life_center) + "║" + (display_trainer_life).rjust(life_center) + "  ║"  )
                print("║  " + HEART + (display_player_hearts).ljust(life_center) + RESET + "║" + HEART + (display_trainer_hearts).rjust(life_center) + RESET + "  ║")
                print("╚══" + ("═══" * MAP_WIDTH) + "══╝")

                print("╔══" + ("═══" * MAP_WIDTH) + "══╗")
                print("║  " + (f"(1){pikachu_attack[0]} (2){pikachu_attack[1]}").center(MAP_WIDTH * 3) + "  ║")
                print("╚══" + ("═══" * MAP_WIDTH) + "══╝")

                attack_option = None
                while attack_option not in ["1", "2"]:
                    attack_option = input(f"\n¿Qué opción desea tomar?: ")
                attack_option = int(attack_option)
                if attack_option == 1:
                    trainer_life -= 10
                    message = f"{pikachu_data[0]} ha usado {pikachu_attack[0]}"
                elif attack_option == 2:
                    trainer_life -= 20
                    message = f"{pikachu_data[0]} ha usado {pikachu_attack[1]}"

                if trainer_life <= 0:
                    os.system("clear")
                    print(WIN_SCREEN)
                    input("")
                    pikachu_data[1] += 10
                    trainer_list = [trainer for trainer in trainer_list if trainer[2] != trainer_combat]
                    end_combat = True
                    
    # Check if the next position is a wall
    if map_definition[next_position[POS_Y]][next_position[POS_X]] != "#":
        character_position = next_position
