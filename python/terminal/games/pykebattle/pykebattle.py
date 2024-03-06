# Importing standard libraries
import random
import os

# Importing local libraries 
from data import get_all_pokemons
from scripts import SCREEN_WIDTH, INPUT_MESSAGE, colorize, print_inside_box, combat_timer, get_pokemon_info, print_pokemon_information, print_actions, player_attack, enemy_attack


POKEMON_LIST = get_all_pokemons() # Fetch all pokemons


def min_lvl_fix():
    for pokemon in POKEMON_LIST:
        for attack in pokemon["attacks"]:
            if attack["min_level"] == "":
                # Set the minimum level to 1 if it's not specified
                attack["min_level"] = 1


def get_player_profile(POKEMON_LIST):
    os.system("clear")
    print_inside_box("Bienvenido, introduce tu nombre")
    return {
        "player_name": input(" > "),
        "pokemon_inventory": [random.choice(POKEMON_LIST) for a in range(3)], # Assign three random pokemons to the player's inventory
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0,
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


#! --------- FUNCTIONS FOR OTHER ACTIONS DURING THE FIGHT --------- !#


def cure_pokemon(player_profile, player_pokemon):
    pass


def capture_with_pokeball(player_profile, enemy_pokemon):
    pass


def item_lottery(player_profile):
    pass


#! --------- FUNCTIONS USED DURING FIGHTS --------- !#


def fight(player_profile, enemy_pokemon):

    attack_history = []
    player_pokemon = choose_pokemon(player_profile)
    print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))

    # The fight continues as long as any player's Pokemon is alive and the enemy Pokemon's health is above 0
    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        
        # The player chooses an action and depending on the action chosen, the player attacks, heals, captures, or changes their Pokemon
        action = print_actions()

        if action == "A":
            player_attack(player_pokemon, enemy_pokemon)
            attack_history.append(player_pokemon)
        elif action == "V":
            cure_pokemon(player_profile, player_pokemon)
        elif action == "P":
            capture_with_pokeball(player_profile, enemy_pokemon)
        elif action == "C":
            player_pokemon = choose_pokemon(player_profile)

        # If the player's Pokemon's health reaches 0 and there are other Pokemons left, the player chooses another Pokemon
        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
            player_pokemon = choose_pokemon(player_profile)

        enemy_attack(enemy_pokemon, player_pokemon)
    
    if enemy_pokemon["current_health"] == 0:
        print("¡Has ganado!")
        assign_experience(attack_history)

    print("--- FIN DEL COMBATE ---")
    input("Presiona ENTER para  continuar...")


def choose_pokemon(player_profile):
    chosen = None
    error = None
    while not chosen:
        os.system("clear")
        print_inside_box("Elije con que pokemon lucharás")

        if error == "Error":
            print("╔" + ("═" * SCREEN_WIDTH) + "╗")
            print("║" + (colorize("ERROR: INGRESA EL NÚMERO CORRESPONDIENTE", "R", True)) + "║")
        else:    
            print("╔" + ("═" * SCREEN_WIDTH) + "╗")
            print("║" + (" " * SCREEN_WIDTH) + "║")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("║" + ("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index]))).center(SCREEN_WIDTH) + "║")
        try:
            print("║" + (" " * SCREEN_WIDTH) + "║")
            print("╚" + ("═" * SCREEN_WIDTH) + "╝")
            return player_profile["pokemon_inventory"][int(input(INPUT_MESSAGE))]
        except (ValueError, IndexError):
            error = "Error"


def assign_experience(attack_history):
    for pokemon in attack_history:
        points = random.randint(1, 5) # Randomly assign experience points between 1 and 5
        pokemon["current_exp"] += points

    while pokemon["current_exp"] > 20: # Level up the pokemon if its current experience is more than 20
        pokemon["current_exp"] <= 20
        pokemon["level"] += 1
        pokemon["current_health"] = pokemon["base_health"]
        print("Tu pokemon ha subido al nivel {}".format(get_pokemon_info(pokemon)))


#! --------- MAIN FUNCTION --------- !#
        

def main():
    player_profile = get_player_profile(POKEMON_LIST)
    min_lvl_fix()
    combat_timer()
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(POKEMON_LIST)
        fight(player_profile, enemy_pokemon)
        item_lottery(player_profile)
    print("Has perdido el combate Nro.{}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()