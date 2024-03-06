
import time
from poke_multiplier import set_multiplier_for_type
from printer import print_in_green, print_in_red,get_move_info,clear_and_header,get_pokemon_info
import random


def print_attacks(player_pokemon):
    attacks_to_print = [attack for attack in player_pokemon["attacks"] if
                        int(attack["min_level"]) <= int(player_pokemon["level"])]
    print("***** MOVIMIENTOS *****\n")

    chosen = None
    while not chosen:
        for index in range(len(attacks_to_print)):
            print("{} - {} ".format(index, get_move_info(attacks_to_print[index])))
        try:
            return attacks_to_print[int(input("¿Cuál eliges?\n"))]
        except (ValueError, IndexError):
            clear_and_header("", "", False)
            print("¡¡¡Opcion invalida!!!")


def player_attack(player_pokemon, enemy_pokemon):
    clear_and_header(player_pokemon, enemy_pokemon, True)
    multiplier = set_multiplier_for_type(player_pokemon, enemy_pokemon)

    attack = print_attacks(player_pokemon)
    clear_and_header(player_pokemon, enemy_pokemon, True)

    print("{} ataca con: {}\n".format(print_in_green(player_pokemon["name"]), attack["name"]))
    time.sleep(2)

    if multiplier > 1:
        print("El ataque fue super efectivo")
        time.sleep(1)
    elif multiplier < 1:
        print("El ataque no ha sido muy efectivo")
        time.sleep(1)

    damage = (int(attack["damage"]) + player_pokemon["attack"] - enemy_pokemon["defense"]) * multiplier
    enemy_pokemon["current_health"] = int(enemy_pokemon["current_health"]) - damage

    print("{} recibe {} puntos de daño (DP)".format(print_in_red(enemy_pokemon["name"]), damage))
    time.sleep(2)

    if int(enemy_pokemon["current_health"]) <= 0:
        enemy_pokemon["current_health"] = 0
        print("{} está fuera de combate.".format(print_in_red(enemy_pokemon["name"])))


def enemy_attack(enemy_pokemon, player_pokemon):
    if int(enemy_pokemon["current_health"]) > 0:

        clear_and_header(player_pokemon, enemy_pokemon, True)
        multiplier = set_multiplier_for_type(enemy_pokemon, player_pokemon)

        attacks = [attack for attack in enemy_pokemon["attacks"] if
                   int(attack["min_level"]) <= int(enemy_pokemon["level"])]

        attack = random.choice(attacks)

        print("{} ataca con: {}\n".format(print_in_red(enemy_pokemon["name"]), attack["name"]))
        time.sleep(2)

        if multiplier > 1:
            print("El ataque fue super efectivo")
            time.sleep(1)
        elif multiplier < 1:
            print("El ataque no ha sido muy efectivo")
            time.sleep(1)

        damage = (int(attack["damage"]) + enemy_pokemon["attack"] - player_pokemon["defense"]) * multiplier
        player_pokemon["current_health"] = int(player_pokemon["current_health"]) - damage

        print("{} recibe {} puntos de daño (DP)".format(print_in_green(player_pokemon["name"]), damage))
        time.sleep(2)

        if int(player_pokemon["current_health"]) <= 0:
            player_pokemon["current_health"] = 0
            print("{} está fuera de combate.".format(print_in_green(player_pokemon["name"])))

        clear_and_header(player_pokemon, enemy_pokemon, True)