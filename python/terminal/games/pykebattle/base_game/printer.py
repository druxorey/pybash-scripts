from colorama import Fore, Style
import os


def get_pokemon_info(pokemon):
    return "{} || lvl {} || HP {}/{}".format(pokemon["name"],
                                             pokemon["level"],
                                             pokemon["current_health"],
                                             pokemon["base_health"])


def get_move_info(attack):
    return " {} || {} DP || Tipo {}".format(attack["name"],
                                            attack["damage"],
                                            attack["type"])


def clear_and_header(player_pokemon, enemy_pokemon, print_stats):
    os.system("clear")
    print("-------------------------")
    print("***** JUEGO POKEMON *****")
    print("-------------------------")
    if print_stats:
        print("Contricantes: \n {} VS {}".format(print_in_green(get_pokemon_info(player_pokemon)),
                                                 print_in_red(get_pokemon_info(enemy_pokemon))))


def print_in_red(string):
    return Fore.RED + string + Style.RESET_ALL


def print_in_green(string):
    return Fore.GREEN + string + Style.RESET_ALL


def print_options():
    action = None

    while action not in ["A", "P", "V", "C"]:
        action = input("¿Qué deseas hacer? \n [A]tacar, [P]okeball, Poción de [V]ida, [C]ambiar\n")

    if action == "A":
        return "A"
    elif action == "V":
        return "V"
    elif action == "P":
        return "P"
    elif action == "C":
        return "C"


