from colorama import Fore, Style
import os
import time


SCREEN_WIDTH = 80


#* Color function
def colorize(string, color, center=False):
    if center:
        string = string.center(SCREEN_WIDTH)
    if color == "R":
        return Fore.RED + string + Style.RESET_ALL
    elif color == "G":
        return Fore.GREEN + string + Style.RESET_ALL
    elif color == "B":
        return Fore.BLUE + string + Style.RESET_ALL


#* Header de la pantalla
def clear_and_header(player_pokemon, enemy_pokemon, print_stats):
    os.system("clear")
    for i in range(3, 0, -1):
        os.system("clear")
        print("╔" + ("═" * SCREEN_WIDTH) + "╗")
        print("║" + (f"NUEVO COMBATE EN {i}").center(SCREEN_WIDTH) + "║")
        print("╚" + ("═" * SCREEN_WIDTH) + "╝")
        # time.sleep(1)


#! Print functions
    
def print_inside_box(string):
    print("╔" + ("═" * SCREEN_WIDTH) + "╗")
    print("║" + string.center(SCREEN_WIDTH) + "║")
    print("╚" + ("═" * SCREEN_WIDTH) + "╝")


def print_pokemon_information(player_pokemon, enemy_pokemon):
    print("╔" + ("═" * SCREEN_WIDTH) + "╗")
    print("║" + (colorize(player_pokemon, "G") + "  VS  " + colorize(enemy_pokemon, "R")).center(SCREEN_WIDTH + 18) + "║")
    print("╚" + ("═" * SCREEN_WIDTH) + "╝")


def get_pokemon_info(pokemon):
    return "{:<10} │ lvl {:<2} │ HP {}/{}".format(pokemon["name"], pokemon["level"], pokemon["current_health"], pokemon["base_health"])

def get_move_info(attack):
    return " {} || {} DP || Tipo {}".format(attack["name"], attack["damage"], attack["type"])


def print_actions():
    action = None
    while action not in ["A", "P", "V", "C"]:
        print_inside_box("[A]tacar, [P]okeball, Poción de [V]ida, [C]ambiar")
        action = input("¿Qué deseas hacer?: ").upper()
    return action