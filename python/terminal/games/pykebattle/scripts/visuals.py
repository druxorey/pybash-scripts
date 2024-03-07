# Importing standard libraries
import os
from colorama import Fore, Style


SCREEN_WIDTH = 80
INPUT_MESSAGE = "\nIngresa tu opción: "


def colorize(string, color, center=False):
    if center:
        string = string.center(SCREEN_WIDTH)
    if color == "R":
        return Fore.RED + string + Style.RESET_ALL
    elif color == "G":
        return Fore.GREEN + string + Style.RESET_ALL
    elif color == "B":
        return Fore.BLUE + string + Style.RESET_ALL


def print_inside_box(string):
    print("╔" + ("═" * SCREEN_WIDTH) + "╗")
    print("║" + string.center(SCREEN_WIDTH) + "║")
    print("╚" + ("═" * SCREEN_WIDTH) + "╝")


def combat_timer():
    os.system("clear")
    for i in range(3, 0, -1): # Print the countdown for the new battle
        os.system("clear")
        print("╔" + ("═" * SCREEN_WIDTH) + "╗")
        print("║" + (f"NUEVO COMBATE EN {i}").center(SCREEN_WIDTH) + "║")
        print("╚" + ("═" * SCREEN_WIDTH) + "╝")
        #!!! time.sleep(1)


def get_pokemon_info(pokemon):
    return "{:<10} │ lvl {:<2} │ HP {:<3}/{:<3}".format(pokemon["name"], pokemon["level"], pokemon["current_health"], pokemon["base_health"])


def get_move_info(attack):
    return " {:<15} || {:<3} DP || Tipo {:<8}".format(attack["name"], attack["damage"], attack["type"])


def print_pokemon_information(player_pokemon, enemy_pokemon):
    os.system("clear")
    print("╔" + ("═" * SCREEN_WIDTH) + "╗")
    print("║" + (colorize(player_pokemon, "G") + "  VS  " + colorize(enemy_pokemon, "R")).center(SCREEN_WIDTH + 18) + "║")
    print("╚" + ("═" * SCREEN_WIDTH) + "╝")


def print_attacks(player_pokemon, enemy_pokemon):
    print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))
    # Get the attacks of the player's Pokemon that are available at its current level
    attacks_to_print = [attack for attack in player_pokemon["attacks"] if int(attack["min_level"]) <= int(player_pokemon["level"])]

    print("╔" + ("═" * SCREEN_WIDTH) + "╗")
    print("║" + ("MOVIMIENTOS").center(SCREEN_WIDTH) + "║")
    print("║" + (" " * SCREEN_WIDTH) + "║")

    # Loop until a valid attack is chosen
    chosen = None
    while not chosen:
        for index in range(len(attacks_to_print)): # Print the available attacks
            print("║" + ("{:<2} - {} ".format(index, get_move_info(attacks_to_print[index]))).center(SCREEN_WIDTH) + "║")
        try:
            print("║" + (" " * SCREEN_WIDTH) + "║")
            print("╚" + ("═" * SCREEN_WIDTH) + "╝")

            return attacks_to_print[int(input(INPUT_MESSAGE))] # Return the chosen attack
        
        except (ValueError, IndexError):
            print("¡¡¡Opcion invalida!!!")


def print_actions():
    action = None
    while action not in ["A", "P", "V", "C"]:
        print_inside_box("[A]tacar, [P]okeball, Poción de [V]ida, [C]ambiar")
        action = input(INPUT_MESSAGE).upper()
    return action