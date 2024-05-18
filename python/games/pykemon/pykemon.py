from colorama import Fore, Style
from visuals import *
import readchar
import os
import random

# Constants for position indexes
POS_X = 0
POS_Y = 1

# Constants for the visual aspects of the game
RESET = f"{Style.RESET_ALL}"
LIMIT = f"{RESET}███"
WALL = f"{Fore.RED}███"
RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE

# Initial values
map_definition = MAP_LAYOUT
character_position = [8,10]
debug_mode = False
display_stadistics = False
display_help = False

# Initial battle values
opponent_list = []
pokemon_life = [60, 70, 95, 120]

# Pikachu's attack names and damage values
pikachu_attack_name = ["Recuperación", "Placaje", "Chispazo", "Trueno"]
pikachu_attack_damage = [20, 10, 18, 36]
pikachu_data = ["Pikachu", pokemon_life[0]]

# Squirtle's attack names and damage values
squirtle_attack = ["Placaje", "Pistola Agua", 12, 18]
squirtle_data = ["Squirtle", pokemon_life[1]]

# Charmeleon's attack names and damage values
charmeleon_attack = ["Ascuas", "Lanzallamas", 25, 35]
charmeleon_data = ["Charmeleon", pokemon_life[2]]

# Venusaur's attack names and damage values
venusaur_attack = ["Latigo Cepa", "Energibola", 32, 48]
venusaur_data = ["Venusaur", pokemon_life[3]]

# Create obstacle map and initialize opponents
map_definition = [list(row) for row in map_definition.split("\n")]
opponent_id = 3
for coordinate_y in range(len(map_definition)):
    for coordinate_x in range(len(map_definition[0])):
        if map_definition[coordinate_y][coordinate_x] == "@":
            opponent_list.append([coordinate_x, coordinate_y, opponent_id])
            opponent_id -= 1
            map_definition[coordinate_y][coordinate_x] = " "

# Constants for map dimensions
MAP_WIDTH = len(map_definition[0])
MAP_HEIGHT = len(map_definition)

# Game start showing the help screen
os.system("clear")
print(HELP_SCREEN)
input("")

# Main game loop
while True:
    # Loop Initial Values
    os.system("clear")
    opponent_combat = None

    # Game map display
    print((LIMIT * MAP_WIDTH) + (LIMIT * 2))
    for coordinate_y in range(MAP_HEIGHT):
        print(LIMIT, end="")
        for coordinate_x in range(MAP_WIDTH):

            # Default character to draw
            char_to_draw = "   "
            char_in_cell = None
            
            # Draw wall's
            if map_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = WALL

            for char_in_cell in opponent_list:
                # Draw opponent's
                if char_in_cell[POS_X] == coordinate_x and char_in_cell[POS_Y] == coordinate_y:
                    char_to_draw = f"{RESET} 󰐝 "
                # Draw character
                if character_position[POS_X] == coordinate_x and character_position[POS_Y] == coordinate_y:
                    char_to_draw = f"{YELLOW}  {RESET}"
                    # Change the value to display the screen start combat message
                    if char_in_cell[POS_X] == character_position[POS_X] and char_in_cell[POS_Y] == character_position[POS_Y]:
                        opponent_combat = char_in_cell[2]
                        break

            print(f"{char_to_draw}", end="")
        print(LIMIT)
    print((LIMIT * MAP_WIDTH) + (LIMIT * 2) + f"\n")

    # Show statistics screen
    if display_stadistics == True:
        print("╔══" + ("═══" * MAP_WIDTH) + "══╗")
        print("║  " + " " * (MAP_WIDTH * 3) + "  ║")
        print("║  " + (f"VIDA: {pikachu_data[1]}").ljust(MAP_WIDTH * 3) + "  ║")
        print("║  " + " " * (MAP_WIDTH * 3) + "  ║")
        print("║  " + (f"ATAQUES: ").ljust(MAP_WIDTH * 3) + "  ║")
        print("║  " + (f"{pikachu_attack_name[0]}: +{pikachu_attack_damage[0]}  {pikachu_attack_name[1]}: {pikachu_attack_damage[1]}").ljust(MAP_WIDTH * 3) + "  ║")
        print("║  " + (f"{pikachu_attack_name[2]}: {pikachu_attack_damage[2]}       {pikachu_attack_name[3]}: {pikachu_attack_damage[3]}").ljust(MAP_WIDTH * 3) + "  ║")
        print("║  " + " " * (MAP_WIDTH * 3) + "  ║")
        print("╚══" + ("═══" * MAP_WIDTH) + "══╝")

    # Show help screen
    if display_help == True:
        os.system("clear")
        print(HELP_SCREEN)    

    # Debug mode
    if debug_mode == True:
        print("character_position: ",character_position)
        print("opponent_combat: ",opponent_list)
        print("pikachu_attack_damage: ",pikachu_attack_damage)
        print("pikachu_data[0]: ",pikachu_data[1])
        print("MAP_WIDTH",MAP_WIDTH)

    # Check if you are on a opponent to ask if you want to fight him
    if opponent_combat is not None:
        print("╔══" + ("═══" * MAP_WIDTH) + "══╗")
        print("║  " + (f"¿Empezar combate contra entrenador Nvl {opponent_combat}? [ENTER]").center(MAP_WIDTH * 3) + "  ║")
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
    elif direction == "e":
        display_stadistics = not display_stadistics
        continue
    elif direction == "h":
        display_help = not display_help
        continue
    elif direction == "b":
        debug_mode = not debug_mode
        continue
    # Start a battle with the opponent if the input is 'Enter'
    elif direction == "\n":    
        if opponent_combat is not None:

            # Select the opponent's Pokemon and attacks based on the opponent's level
            if opponent_combat == 1:
                opponent_pokemon = [squirtle_data[0], squirtle_data[1]] 
                opponent_attack = [squirtle_attack[0], squirtle_attack[1], squirtle_attack[2], squirtle_attack[3]]
            elif opponent_combat == 2:
                opponent_pokemon = [charmeleon_data[0], charmeleon_data[1]]
                opponent_attack = [charmeleon_attack[0], charmeleon_attack[1], charmeleon_attack[2], charmeleon_attack[3]]
            elif opponent_combat == 3:
                opponent_pokemon = [venusaur_data[0], venusaur_data[1]]
                opponent_attack = [venusaur_attack[0], venusaur_attack[1], venusaur_attack[2], venusaur_attack[3]]

            # Variables are established for combat
            player_life = pikachu_data[1]
            opponent_life = opponent_pokemon[1]
            set_turn = 1

            message = f"Entrenador saca a {opponent_pokemon[0]}"
            end_combat = None
            while end_combat != True:
                os.system("clear")

                life_center = int((MAP_WIDTH*3)/2)

                # Display the player's and opponent's Pokemon's life
                display_player_life = f"{pikachu_data[0]} Ps.{player_life}/{pikachu_data[1]}"
                display_opponent_life = f"{opponent_pokemon[0]} Ps.{opponent_life}/{opponent_pokemon[1]}"
                # Display the player's and opponent's Pokemon's life
                display_player_REDs = " " * (int(player_life / pikachu_data[1] * 10)) 
                display_opponent_REDs = " " * (int(opponent_life / opponent_pokemon[1] * 10)) 

                # Print the battle screen
                print("╔══" + ("═══" * MAP_WIDTH) + "══╗")
                print("║  " + message.center(MAP_WIDTH * 3) + "  ║")
                print("╚══" + ("═══" * MAP_WIDTH) + "══╝")

                print("╔══"+("═══" * MAP_WIDTH) + "══╗")
                print("║  "+YELLOW +(display_player_life).ljust(life_center)+RESET+"║"+BLUE+(display_opponent_life).rjust(life_center)+RESET+"  ║")
                print("║  "+RED+(display_player_REDs).ljust(life_center)+RESET+"║"+RED+(display_opponent_REDs).rjust(life_center)+RESET+"  ║")
                print("╚══" + ("═══" * MAP_WIDTH) + "══╝")

                # Player turn
                if set_turn == 1:
                    set_turn = 2
                    
                    # Display the player's Pokemon's attacks
                    print("╔══" + ("═══" * MAP_WIDTH) + "══╗")
                    print("║  " + (f"(1){pikachu_attack_name[0]} (2){pikachu_attack_name[1]}").center(MAP_WIDTH * 3) + "  ║")
                    print("║  " + (f"(3){pikachu_attack_name[2]} (4){pikachu_attack_name[3]}").center(MAP_WIDTH * 3) + "  ║")
                    print("╚══" + ("═══" * MAP_WIDTH) + "══╝")

                    # Ask the player to choose an attack option
                    attack_option = None
                    while attack_option not in ["1", "2", "3", "4"]:
                        attack_option = input(f"\n¿Qué opción desea tomar?: ")
                    attack_option = int(attack_option)

                    #The first attack recovers up to maximum health, if used with maximum health it fails
                    if attack_option == 1:
                        if player_life < pikachu_data[1]:
                            recover_amount = min(pikachu_attack_damage[0], pikachu_data[1] - player_life)
                            player_life += recover_amount
                            message = f"{pikachu_data[0]} ha usado {pikachu_attack_name[0]}"
                        else:
                            player_life = pikachu_data[1]
                            message = f"{pikachu_data[0]} ha fallado usando {pikachu_attack_name[0]}"

                    # The second attack does damage
                    elif attack_option == 2:
                        opponent_life -= pikachu_attack_damage[1]
                        message = f"{pikachu_data[0]} ha usado {pikachu_attack_name[1]}"

                    # The third attack does damage
                    elif attack_option == 3:
                        opponent_life -= pikachu_attack_damage[2]
                        message = f"{pikachu_data[0]} ha usado {pikachu_attack_name[2]}"
                    
                    # The fourth attack has a 50% chance to miss or hit
                    elif attack_option == 4:
                        precision = random.randint(1,2)
                        if precision == 1:
                            opponent_life -= pikachu_attack_damage[3]
                            message = f"{pikachu_data[0]} ha usado {pikachu_attack_name[3]}"
                        else:
                            message = f"{pikachu_data[0]} ha fallado usando {pikachu_attack_name[3]}"
                    
                    # If the health of the rival opponent reaches 0, the player wins, his statistics increase and the rival is eliminated from the map
                    if opponent_life <= 0:
                        os.system("clear")
                        print(WIN_SCREEN)
                        input("")
                        pikachu_data[1] += 16
                        pikachu_attack_damage = [x + 13 for x in pikachu_attack_damage]
                        opponent_list = [opponent for opponent in opponent_list if opponent[2] != opponent_combat]
                        end_combat = True

                # Oponent turn
                elif set_turn == 2:
                    set_turn = 1

                    # Shows that it is the opponent's pokemon's turn
                    print("╔══" + ("═══" * MAP_WIDTH) + "══╗")
                    print("║  " + BLUE + (f"Es el turno de {opponent_pokemon[0]}").center(MAP_WIDTH * 3) + RESET + "  ║")
                    print("╚══" + ("═══" * MAP_WIDTH) + "══╝")

                    input(f"\nENTER para continuar")

                    # The oponent chooses an attack randomly
                    attack_chose = random.randint(1,2)
                    if attack_chose == 1:
                        player_life -= opponent_attack[2]
                        message = f"{opponent_pokemon[0]} ha usado {opponent_attack[0]}"
                    elif attack_chose == 2:
                        player_life -= opponent_attack[3]
                        message = f"{opponent_pokemon[0]} ha usado {opponent_attack[1]}"

                    # If the player's health reaches 0 they lose
                    if player_life <= 0:
                        os.system("clear")
                        print(LOSE_SCREEN)
                        input("")
                        end_combat = True
    
    # If all opponents are eliminated, the player wins and the game is over.
    if not opponent_list:
        os.system("clear")
        print(WINNER_SCREEN)
        exit()
                    
    # Check if the next position is a wall
    if map_definition[next_position[POS_Y]][next_position[POS_X]] != "#":
        character_position = next_position
