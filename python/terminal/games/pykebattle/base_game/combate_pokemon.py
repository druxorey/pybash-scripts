import random
import time

from pokeload import get_all_poke
from printer import get_pokemon_info, clear_and_header, print_options, print_in_green, print_in_red
from attack_mechanism import player_attack, enemy_attack

POKEMON_LIST = get_all_poke()


def get_player_profile(pokemon_list):
    return {
        "player_name": input("¿Cual es tu nombre?\n"),
        "pokemon_inv": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 5,
        "health_potion": 2
    }


def print_and_wait(message, wait_time):
    print(message)
    time.sleep(wait_time)


def choose_pokemon(player_profile):
    clear_and_header("", "", False)
    chosen = None
    while not chosen:
        print("***** SELECT POKEMON *****")

        for index in range(len(player_profile["pokemon_inv"])):
            print("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inv"][index])))
        try:
            eleccion = int(input("¿Cuál eliges?\n"))
            if player_profile["pokemon_inv"][eleccion]["current_health"] > 0:
                return player_profile["pokemon_inv"][eleccion]
            else:
                clear_and_header("", "", False)
                print("¡¡¡Pokemon derrotado!!!")
        except (ValueError, IndexError):
            clear_and_header("", "", False)
            print("¡¡¡Opcion invalida!!!")


def assign_exp(attack_history):
    for pokemon in attack_history:
        # Asigna de 2 a 8 pts de exp por cada ataque
        points = random.randint(2, 8)
        print("{} ha ganado {} pts de exp".format(print_in_green(pokemon["name"]), points))
        pokemon["current_exp"] += points

        # Experiencia necesaria para subir de nivel  = 20 + (nivel de pokemon * 2)
        exp_needed = 20 + (pokemon["level"] * 2)

        while pokemon["current_exp"] > exp_needed:
            print("¡{} subió al nivel {}!".format(print_in_green(pokemon["name"]), pokemon["level"] + 1))
            pokemon["current_exp"] -= exp_needed
            pokemon["level"] += 1
            # Aumenta el ataque, prob 80%, aumento de 1-2 pts
            if random.randint(1, 100) > 20:
                attack_increase = random.randint(1, 2)
                pokemon["attack"] += attack_increase
                print(" Ataque aumentado en {} Pts, total: {}".format(attack_increase, pokemon["attack"]))
            # Aumenta la defensa, prob 80%, aumento de 1-2 pts
            if random.randint(1, 100) > 20:
                defense_increase = random.randint(1, 2)
                pokemon["defense"] += defense_increase
                print(" Defensa aumentada en {} Pts, total: {}".format(defense_increase, pokemon["defense"]))

            # Aumenta la VUDA, prob 80%, aumento de 3-6 pts
            if random.randint(1, 100) > 20:
                health_increase = random.randint(3, 6)
                pokemon["base_health"] += health_increase
                print(" Vida aumentada en {} Pts, total: {}".format(health_increase, pokemon["base_health"]))

            pokemon["current_health"] = pokemon["base_health"]
            input("Enter para continuar")


def cure_pokemon(player_pokemon, player_profile):
    # Muestra cantidad pociones

    print_and_wait("Tienes {} pociones".format(player_profile["health_potion"]),1)

    # Verifica que existan pociones
    if player_profile["health_potion"] > 0:
        recovered_points = player_pokemon["base_health"] - player_pokemon["current_health"]
        if recovered_points > 50:
            recovered_points = 50

        player_pokemon["current_health"] += 50

        if player_pokemon["current_health"] > player_pokemon["base_health"]:
            player_pokemon["current_health"] = player_pokemon["base_health"]

        # Resta una pocion del inv
        player_profile["health_potion"] -= 1
        print_and_wait("Utilizaste una poción",1)

        # Muestra los pts recuperados
        print_and_wait("{} Pts recuperados.".format(recovered_points), 1)


# Determina la probabilidad a partir de la vida, devuelve true o false dependiendo
# si el pokemon fue vencido
def capture_pokemon(enemy_pokemon, player_profile):
    probability = ((enemy_pokemon["current_health"] / enemy_pokemon["base_health"]) * 100)
    print_and_wait("Lanzaste una pokeball", 1)
    player_profile["pokeballs"] -= 1
    print_and_wait("Tick...", 1)
    print_and_wait("Tick...", 1)
    if random.randint(1, 100) > probability:
        print_and_wait("Tick...", 1)
        print_and_wait("puff...", 1)
        player_profile["pokemon_inv"].append(enemy_pokemon)
        print_and_wait("¡{} ha sido atrapado!".format(print_in_red(enemy_pokemon["name"])), 1)
        print_and_wait("Te quedan {} pokeballs".format(player_profile["pokeballs"]), 2)
        return True
    else:
        print_and_wait("Tick...", 1)
        print("¡Oh no!\n")
        print_and_wait("¡El pokemon ha escapado de la pokebola!", 1)
        print_and_wait("Te quedan {} pokeballs".format(player_profile["pokeballs"]), 2)
        return False


def fight(player_profile, enemy_pokemon):
    clear_and_header("", "", False)
    print("--- NUEVO COMBATE---\n")

    attack_history = []

    # Escoge pokemon
    player_pokemon = choose_pokemon(player_profile)
    clear_and_header("", "", False)
    enemy_captured = False
    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0 and not enemy_captured:
        # Muestra opciones y registra seleccion
        action = print_options()

        if action == "A":
            player_attack(player_pokemon, enemy_pokemon)
            attack_history.append(player_pokemon)
        elif action == "V":
            if player_profile["health_potion"] > 0:
                cure_pokemon(player_pokemon, player_profile)
            else:
                print_and_wait("No tienes pociones, pierdes turno",2)
        elif action == "P":
            if len(player_profile["pokemon_inv"]) >= 6:
                print_and_wait("Ya tienes 6 pokemons en tu equipo, pierdes turno, avaricioso.",2)
            else:
                if player_profile["pokeballs"] > 0:
                    enemy_captured = capture_pokemon(enemy_pokemon, player_profile)
                else:
                    print_and_wait("No tienes pokeballs, pierdes turno",2)
        elif action == "C":
            player_pokemon = choose_pokemon(player_profile)
            print("Has elegido a {}".format(player_pokemon["name"]))

        if not enemy_captured:
            enemy_attack(enemy_pokemon, player_pokemon)

        # Si nuestro pokemon muere
        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
            player_pokemon = choose_pokemon(player_profile)

    # Si el pokemon enemigo ha muerto
    if enemy_pokemon["current_health"] == 0 or enemy_captured:
        print("{} ha ganado!".format(print_in_green(player_profile["player_name"])))
        player_profile["combats"] = int(player_profile["combats"]) + 1
        print("Combates: {}".format(player_profile["combats"]))
        assign_exp(attack_history)

    print("--- FIN del  COMBATE---\n")
    input("Presiona enter para continuar")


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inv"]]) > 0


def item_lottery(player_profile):
    # 50% de prob de obtener una potion y 50% de una pokeball
    clear_and_header("", "", False)

    item = random.randint(1, 2)
    if item == 1:
        player_profile["pokeballs"] += 1
        print_and_wait("Obtuviste una pokeball, tienes {}".format(player_profile["pokeballs"]),2)
    else:
        player_profile["health_potion"] += 1
        print_and_wait("Obtuviste una poción, tienes {}".format(player_profile["health_potion"]),2)


# Arregla los ataquees de pokemons con min level vacio ('')
def fix_pokemon_list():
    cont_a = 0
    for a in POKEMON_LIST:
        cont_b = 0
        for attack in a["attacks"]:
            if attack["min_level"] == "":
                POKEMON_LIST[cont_a]["attacks"][cont_b]["min_level"] = 1
            cont_b += 1
        cont_a += 1


def main():
    clear_and_header("", "", False)
    fix_pokemon_list()
    player_profile = get_player_profile(POKEMON_LIST)
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(POKEMON_LIST)
        fight(player_profile, enemy_pokemon)
        item_lottery(player_profile)

    clear_and_header("", "", False)
    print("Has perdido el combate #{}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()
