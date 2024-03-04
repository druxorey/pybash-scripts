from pokeload import get_all_pokemons

def get_player_profile(pokemon_list):
    return {
        "player_name": input("¿Cuál es tu nombre?: ")
        "pokemon_inventory": []
    }

def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile()

if __name__ == "__main__":
    main()
