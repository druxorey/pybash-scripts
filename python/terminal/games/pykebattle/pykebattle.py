from pokeload import get_all_pokemons
import random

from pprint import pprint


def get_player_profile(pokemon_list):
    return {
        "player_name": input("¿Cuál es tu nombre?: "),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0,
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def choose_pokemon(player_profile):
    chosen = None
    while not chosen:
        print("Elije con que pokemon lucharás")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))
        try:
            return player_profile["pokemon_inventory"][int(input("¿Cuál eliges?: "))]
        except (ValueError, IndexError):
            print("Elección inválida")


def get_pokemon_info(pokemon):
    return "{} | lvl {} | HP {}/{}".format(pokemon["name"], pokemon["level"], pokemon["current_health"], pokemon["base_health"])


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
    print("--- NUEVO COMBATE ---")

    attack_history = []
    player_pokemon = choose_pokemon(player_profile)
    print("Rivales: {} VS {}".format(get_pokemon_info(player_pokemon), get_pokemon_info(enemy_pokemon)))
    
    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        action = None
        while action not in ["A", "P", "V", "C"]:
            action = input("¿Qué deseas hacer?: [A]tacar, [P]okeball, Poción de [V]ida, [C]ambiar\n")

        if action == "A":
            player_attack(player_pokemon, enemy_pokemon)
            attack_history.append(player_pokemon)
            enemy_attack(enemy_pokemon, player_pokemon)
        elif action == "V":
            cure_pokemon(player_profile, player_pokemon)
        elif action == "P":
            capture_with_pokeball(player_profile, enemy_pokemon)

        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
            player_pokemon = choose_pokemon(player_profile)
    
    if enemy_pokemon["current_health"] == 0:
        print("¡Has ganado!")
        assign_experience()

    print("--- FIN DEL COMBATE ---")
    input("Presiona ENTER para  continuar...")


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)
    print("Has perdido el combate Nro.{}".format(player_profile["combats"]))

if __name__ == "__main__":
    main()
