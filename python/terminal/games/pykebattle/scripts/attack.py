# Importing standard libraries
import time
import random

# Importing local libraries 
from data import multiplier_for_type
from .visuals import colorize, print_pokemon_information, get_pokemon_info, print_attacks


def attack_information(attacking_pokemon, defending_pokemon, multiplier, attack, is_player):
    if is_player:
        attacking_pokemon_color = "G"
        defending_pokemon_color = "R"
    else:
        attacking_pokemon_color = "R"
        defending_pokemon_color = "G"
    print("{} ataca con: {}\n".format(colorize(attacking_pokemon["name"], attacking_pokemon_color), attack["name"]))
    if multiplier > 1:
        print("El ataque fue super efectivo")
        time.sleep(1)
    elif multiplier < 1:
        print("El ataque no ha sido muy efectivo")
        time.sleep(1)

    damage = (int(attack["damage"]) + attacking_pokemon["attack"] - defending_pokemon["defense"]) * multiplier
    defending_pokemon["current_health"] = int(defending_pokemon["current_health"]) - damage

    print("{} recibe {} puntos de daño (DP)".format(colorize(defending_pokemon["name"], defending_pokemon_color), damage))
    time.sleep(2)

    if int(defending_pokemon["current_health"]) <= 0:
        defending_pokemon["current_health"] = 0
        print("{} está fuera de combate.".format(colorize(defending_pokemon["name"], defending_pokemon_color)))


def player_attack(player_pokemon, enemy_pokemon):
    
    multiplier = multiplier_for_type(player_pokemon, enemy_pokemon)
    attack = print_attacks(player_pokemon, enemy_pokemon)
    
    print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))
    attack_information(player_pokemon, enemy_pokemon, multiplier, attack, is_player=True)
    

def enemy_attack(enemy_pokemon, player_pokemon):
    if int(enemy_pokemon["current_health"]) > 0:

        multiplier = multiplier_for_type(enemy_pokemon, player_pokemon)
        attacks = [attack for attack in enemy_pokemon["attacks"] if
                   int(attack["min_level"]) <= int(enemy_pokemon["level"])]
        attack = random.choice(attacks)

        print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))
        attack_information(enemy_pokemon, player_pokemon, multiplier, attack, is_player=False)