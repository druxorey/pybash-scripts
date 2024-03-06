from scripts import *
from data import *
import random
import time


POKEMON_LIST = get_all_pokemons()


def get_player_profile(POKEMON_LIST):
    os.system("clear")
    print_inside_box("Bienvenido, introduce tu nombre")
    return {
        "player_name": input(" > "),
        "pokemon_inventory": [random.choice(POKEMON_LIST) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0,
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def choose_pokemon(player_profile):
    chosen = None
    error = None
    while not chosen:
        os.system("clear")
        print_inside_box("Elije con que pokemon lucharás")
        # Manejar errroes
        if error == "Error":
            print("\n" + (colorize("ERROR: INGRESA LOS DATOS CORRECTAMENTE", "R", True)) + "\n")
        else:    
            print("")
        # Imprimir lista de pokemon actuales
        for index in range(len(player_profile["pokemon_inventory"])):
            print("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))
        try:
            return player_profile["pokemon_inventory"][int(input("\n¿Cuál eliges?: "))]
        except (ValueError, IndexError):
            error = "Error"

#! SECONDARY FIGHT FUNCTIONS

def player_attack(player_pokemon, enemy_pokemon):
    pass


def enemy_attack(enemy_pokemon, player_pokemon):
    pass


def assign_experience(attack_history):
    for pokemon in attack_history:
        points = random.randint(1, 5) 
        pokemon["current_exp"] += points
    
    while pokemon["current_exp"] > 20:
        pokemon["current_exp"] <= 20
        pokemon["level"] += 1
        pokemon["current_health"] = pokemon["base_health"]
        print("Tu pokemon ha subido al nivel {}".format(get_pokemon_info(pokemon)))


def cure_pokemon(player_profile, player_pokemon):
    pass


def capture_with_pokeball(player_profile, enemy_pokemon):
    pass

#! PRINCIPAL FIGHT FUNCTION

def fight(player_profile, enemy_pokemon):

    attack_history = []
    player_pokemon = choose_pokemon(player_profile)
    os.system("clear")

    print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))
    
    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        action = None
        while action not in ["A", "P", "V", "C"]:
            action = input("¿Qué deseas hacer?: [A]tacar, [P]okeball, Poción de [V]ida, [C]ambiar\n")

        if action == "A":
            player_attack(player_pokemon, enemy_pokemon)
            attack_history.append(player_pokemon)
        elif action == "V":
            cure_pokemon(player_profile, player_pokemon)
        elif action == "P":
            capture_with_pokeball(player_profile, enemy_pokemon)
        elif action == "C":
            player_pokemon = choose_pokemon(player_profile)

        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
            player_pokemon = choose_pokemon(player_profile)
        
        enemy_attack(enemy_pokemon, player_pokemon)
    
    if enemy_pokemon["current_health"] == 0:
        print("¡Has ganado!")
        assign_experience()

    print("--- FIN DEL COMBATE ---")
    input("Presiona ENTER para  continuar...")


def item_lottery(player_profile):
    pass

# Arregla el nivel de los pokemon 
def min_lvl_fix():
    for pokemon in POKEMON_LIST:
        for attack in pokemon["attacks"]:
            if attack["min_level"] == "":
                attack["min_level"] = 1

#! MAIN FUNCTION

def main():
    player_profile = get_player_profile(POKEMON_LIST)
    clear_and_header("", "", False)
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(POKEMON_LIST)
        fight(player_profile, enemy_pokemon)
        item_lottery(player_profile)
    print("Has perdido el combate Nro.{}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()