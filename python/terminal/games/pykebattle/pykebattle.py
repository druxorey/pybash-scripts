# Importing standard libraries
import random
import time
import os

# Importing local libraries 
from data import get_all_pokemons
from scripts import SCREEN_WIDTH, INPUT_MESSAGE, colorize, print_inside_box, after_combat_status, get_pokemon_info, print_pokemon_information, print_actions, player_attack, enemy_attack


# FUNCIONES PARA INICIALIZAR EL JUEGO


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
        "combats": 1,
        "pokeballs": 10,
        "health_potion": 3,
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


#! --------- FUNCTIONS FOR THE ACTIONS AFTER THE FIGHT --------- !#


def item_lottery(player_profile):
    item = random.randint(1, 2)
    os.system("clear")
    if item == 1:
        player_profile["pokeballs"] += 1
        item_obtained = "Obtuviste una pokeball, tienes {}".format(player_profile["pokeballs"])
    else:
        player_profile["health_potion"] += 1
        item_obtained = "Obtuviste una poción, tienes {}".format(player_profile["health_potion"])
    return item_obtained


def assign_experience(attack_history):
    experience_gained = []
    total_points = 0  # Inicializa el total de puntos de experiencia ganados
    for pokemon in attack_history:

        # Asigna de 2 a 8 pts de exp por cada ataque
        points = random.randint(8, 10)
        total_points += points
        pokemon["current_exp"] += points

        # Experiencia necesaria para subir de nivel  = 20 + (nivel de pokemon * 2)
        exp_needed = 20 + (pokemon["level"] * 2)
        while pokemon["current_exp"] > exp_needed:
            pokemon["current_exp"] -= exp_needed
            pokemon["level"] += 1
            experience_gained.append("¡{} subió al nivel {}!".format(colorize(pokemon["name"], "G"), 
                                                                     pokemon["level"]))

            # Aumenta el ataque, prob 80%, aumento de 1-2 pts
            if random.randint(1, 100) > 20:
                attack_increase = random.randint(1, 2)
                pokemon["attack"] += attack_increase
                experience_gained.append("Ataque de {} aumentado en {} Pts, total: {}".format(colorize(pokemon["name"], "G"), 
                                                                                              attack_increase, pokemon["attack"]))

            # Aumenta la defensa, prob 80%, aumento de 1-2 pts
            if random.randint(1, 100) > 20:
                defense_increase = random.randint(1, 2)
                pokemon["defense"] += defense_increase
                experience_gained.append("Defensa de {} aumentada en {} Pts, total: {}".format(colorize(pokemon["name"], "G"), 
                                                                                               defense_increase, pokemon["defense"]))

            # Aumenta la vida, prob 80%, aumento de 3-6 pts
            if random.randint(1, 100) > 20:
                health_increase = random.randint(3, 6)
                pokemon["base_health"] += health_increase
                experience_gained.append("Vida de {} aumentada en {} Pts, total: {}".format(colorize(pokemon["name"], "G"), 
                                                                                            health_increase, pokemon["base_health"]))

            # Sube la vida al máximo
            pokemon["current_health"] = pokemon["base_health"]

    # Agrega el mensaje de experiencia ganada al final del ciclo para cada Pokémon
    experience_gained.insert(0, "{} ha ganado {} pts de exp".format(colorize(pokemon["name"], "G"), total_points))

    return experience_gained


#! --------- FUNCTIONS USED DURING FIGHTS --------- !#


def fight(player_profile, enemy_pokemon):

    attack_history = []
    enemy_captured = False
    player_pokemon = choose_pokemon(player_profile, enemy_pokemon)
    print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))

    # The fight continues as long as any player's Pokemon is alive and the enemy Pokemon's health is above 0
    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0 and not enemy_captured:
        
        # The player chooses an action and depending on the action chosen, the player attacks, heals, captures, or changes their Pokemon
        action = print_actions(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))

        if action == "A":
            player_attack(player_pokemon, enemy_pokemon)
            attack_history.append(player_pokemon)
        elif action == "V":
            cure_pokemon(player_profile, player_pokemon, enemy_pokemon)
        elif action == "P":
            enemy_captured = capture_with_pokeball(player_profile, enemy_pokemon)
        elif action == "C":
            player_pokemon = choose_pokemon(player_profile, enemy_pokemon)

        if not enemy_captured:
            enemy_attack(enemy_pokemon, player_pokemon)

        # If the player's Pokemon's health reaches 0 and there are other Pokemons left, the player chooses another Pokemon
        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
            player_pokemon = choose_pokemon(player_profile, enemy_pokemon)

    
    if enemy_pokemon["current_health"] == 0:
        experience_gained = assign_experience(attack_history)
        item_obtained = item_lottery(player_profile)
        after_combat_status(experience_gained, item_obtained)
        player_profile["combats"] = int(player_profile["combats"]) + 1


def choose_pokemon(player_profile, enemy_pokemon):
    chosen = None
    error_message = None
    while not chosen:
        os.system("clear")
        print_inside_box("Vas a luchar contra {}".format(enemy_pokemon["name"]))

        print("╔" + ("═" * SCREEN_WIDTH) + "╗")
        print("║" + (" " * SCREEN_WIDTH) + "║")
        if error_message:
            print("║" + (colorize(f"ERROR: {error_message}", "R", True)) + "║")
        else:    
            print("║" + "ELIGE TU POKÉMON".center(SCREEN_WIDTH) + "║")
        print("║" + (" " * SCREEN_WIDTH) + "║")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("║" + ("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index]))).center(SCREEN_WIDTH) + "║")
        try:
            print("║" + (" " * SCREEN_WIDTH) + "║")
            print("╚" + ("═" * SCREEN_WIDTH) + "╝")
            
            choice =  player_profile["pokemon_inventory"][int(input(INPUT_MESSAGE))]

            if choice["current_health"] > 0:
                return choice
            else:
                error_message = "ESE POKÉMON HA SIDO DERROTADO"
             
        except (ValueError, IndexError):
            error_message = "INTRODUCE UNA OPCIÓN VÁLIDA"


def cure_pokemon(player_profile, player_pokemon, enemy_pokemon):
    print_pokemon_information(get_pokemon_info(player_pokemon), (get_pokemon_info(enemy_pokemon)))

    if player_profile["health_potion"] > 0:
        recovered_points = min(50, player_pokemon["base_health"] - player_pokemon["current_health"])
        player_pokemon["current_health"] = min(player_pokemon["base_health"], player_pokemon["current_health"] + 50)
        player_profile["health_potion"] -= 1

        print("╔" + ("═" * SCREEN_WIDTH) + "╗")
        print("║" + (("Tienes {} pociones".format(player_profile["health_potion"])).center(SCREEN_WIDTH)) + "║")
        print("║" + "Utilizaste una poción".center(SCREEN_WIDTH) + "║")
        print("║" + ("{} Pts recuperados.".format(recovered_points)).center(SCREEN_WIDTH) + "║")
        print("╚" + ("═" * SCREEN_WIDTH) + "╝")
    else:
        print_inside_box("No tienes más pociones.")
    time.sleep(3)


def capture_with_pokeball(player_profile, enemy_pokemon):
    def wait(message, wait_time):
            print(message)
            time.sleep(wait_time)

    probability = ((enemy_pokemon["current_health"] / enemy_pokemon["base_health"]) * 100)
    print("Lanzaste una pokeball")
    player_profile["pokeballs"] -= 1
    wait("Tick...", 1)
    wait("Tick...", 1)
    if random.randint(1, 100) > probability:
        wait("Tick...", 1)
        wait("puff...", 1)
        player_profile["pokemon_inventory"].append(enemy_pokemon)
        wait("¡{} ha sido atrapado!".format(colorize(enemy_pokemon["name"], "R")), 1)
        wait("Te quedan {} pokeballs".format(player_profile["pokeballs"]), 2)
        # presiona enter 
        return True
    else:
        wait("Tick...", 1)
        print("¡Oh no!\n")
        wait("¡El pokemon ha escapado de la pokebola!", 1)
        wait("Te quedan {} pokeballs".format(player_profile["pokeballs"]), 2)
        return False


#! --------- MAIN FUNCTION --------- !#
        

def main():
    player_profile = get_player_profile(POKEMON_LIST)
    min_lvl_fix()
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(POKEMON_LIST)
        fight(player_profile, enemy_pokemon)
    os.system("clear")
    print_inside_box("Has perdido el combate Nro.{}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()