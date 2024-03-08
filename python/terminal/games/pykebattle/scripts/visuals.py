# Importing standard libraries
import os
import time
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


def print_inside_box(string):
    print("╔" + ("═" * SCREEN_WIDTH) + "╗")
    print("║" + string.center(SCREEN_WIDTH) + "║")
    print("╚" + ("═" * SCREEN_WIDTH) + "╝")


def after_combat_status(experience_gained, item_obtained):
    os.system("clear")
    print_inside_box("¡HAS GANADO! Presiona ENTER para continuar...")

    print("╔" + ("═" * SCREEN_WIDTH) + "╗")
    print("║" + (" " * SCREEN_WIDTH) + "║")
    for experience in experience_gained:
        print("║" + experience.center(SCREEN_WIDTH + 9) + "║")
    print("║" + (" " * SCREEN_WIDTH) + "║")
    print("╚" + ("═" * SCREEN_WIDTH) + "╝")
    input()

    for i in range(3, 0, -1): # Print the countdown for the new battle
        os.system("clear")
        print_inside_box("NUEVO COMBATE EN {}".format(i))
        print_inside_box(item_obtained)
        time.sleep(1)


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
    # Get the attacks of the player's Pokemon that are available at its current level
    attacks_to_print = [attack for attack in player_pokemon["attacks"] if int(attack["min_level"]) <= int(player_pokemon["level"])]
    # Loop until a valid attack is chosen
    chosen = None
    while not chosen:
        print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))

        print("╔" + ("═" * SCREEN_WIDTH) + "╗")
        print("║" + (" " * SCREEN_WIDTH) + "║")
        print("║" + ("MOVIMIENTOS").center(SCREEN_WIDTH) + "║")
        print("║" + (" " * SCREEN_WIDTH) + "║")
        for index in range(len(attacks_to_print)): # Print the available attacks
            print("║" + ("{:<2} - {} ".format(index, get_move_info(attacks_to_print[index]))).center(SCREEN_WIDTH) + "║")
        try:
            print("║" + (" " * SCREEN_WIDTH) + "║")
            print("╚" + ("═" * SCREEN_WIDTH) + "╝")

            return attacks_to_print[int(input(INPUT_MESSAGE))] # Return the chosen attack
        
        except (ValueError, IndexError):
            pass


def print_actions(player_pokemon, enemy_pokemon):
    action = None
    while action not in ["A", "P", "V", "C"]:
        print_pokemon_information(player_pokemon, enemy_pokemon)
        print_inside_box("[A]tacar, [P]okeball, Poción de [V]ida, [C]ambiar")
        action = input(INPUT_MESSAGE).upper()
    return action