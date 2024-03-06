# Importing standard libraries
import time
import random

# Importing local libraries 
from data import multiplier_for_type
from .visuals import colorize, print_pokemon_information, get_pokemon_info, print_attacks


def player_attack(player_pokemon, enemy_pokemon):
    print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))
    multiplier = multiplier_for_type(player_pokemon, enemy_pokemon)
    attack = print_attacks(player_pokemon)
    print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))

    print("{} ataca con: {}\n".format(colorize(player_pokemon["name"], "G"), attack["name"]))
    time.sleep(2)

    if multiplier > 1:
        print("El ataque fue super efectivo")
        time.sleep(1)
    elif multiplier < 1:
        print("El ataque no ha sido muy efectivo")
        time.sleep(1)

    damage = (int(attack["damage"]) + player_pokemon["attack"] - enemy_pokemon["defense"]) * multiplier
    enemy_pokemon["current_health"] = int(enemy_pokemon["current_health"]) - damage

    print("{} recibe {} puntos de daño (DP)".format(colorize(enemy_pokemon["name"], "R"), damage))
    time.sleep(2)

    if int(enemy_pokemon["current_health"]) <= 0:
        enemy_pokemon["current_health"] = 0
        print("{} está fuera de combate.".format(colorize(enemy_pokemon["name"], "R")))


def enemy_attack(enemy_pokemon, player_pokemon):
    if int(enemy_pokemon["current_health"]) > 0:

        print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))
        multiplier = multiplier_for_type(enemy_pokemon, player_pokemon)

        attacks = [attack for attack in enemy_pokemon["attacks"] if
                   int(attack["min_level"]) <= int(enemy_pokemon["level"])]

        attack = random.choice(attacks)

        print("{} ataca con: {}\n".format(colorize(enemy_pokemon["name"], "R"), attack["name"]))
        time.sleep(2)

        if multiplier > 1:
            print("El ataque fue super efectivo")
            time.sleep(1)
        elif multiplier < 1:
            print("El ataque no ha sido muy efectivo")
            time.sleep(1)

        damage = (int(attack["damage"]) + enemy_pokemon["attack"] - player_pokemon["defense"]) * multiplier
        player_pokemon["current_health"] = int(player_pokemon["current_health"]) - damage

        print("{} recibe {} puntos de daño (DP)".format(colorize(player_pokemon["name"], "G"), damage))
        time.sleep(2)

        if int(player_pokemon["current_health"]) <= 0:
            player_pokemon["current_health"] = 0
            print("{} está fuera de combate.".format(colorize(player_pokemon["name"], "G")))

        print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))