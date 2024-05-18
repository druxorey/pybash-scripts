from requests_html import HTMLSession
import pickle
import sys
import os

URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="
PKBASE = {
    "name": "",
    "current_health": 100,
    "base_health": 100,
    "level": 5,
    "type": None,
    "current_exp": 0,
    "defense": 10,
    "attack" : 10
}

# Get the path of the current directory and join the current directory path with the file name
current_dir = os.path.dirname(os.path.abspath(__file__))
pokefile_path = os.path.join(current_dir, "pokefile.pkl")


# Function to get Pokemon data from the website specified in the URL_BASE
def get_pokemon(index):
    url = "{}{}".format(URL_BASE, index)
    session = HTMLSession()
    page = session.get(url)

    # Copy the base Pokemon properties
    new_pokemon = PKBASE.copy()

    # Extract the Pokemon name
    new_pokemon["name"] = page.html.find(".mini", first=True).text.split("\n")[0]
    
    # Extract the Pokemon type(s)
    new_pokemon["type"] = []
    for img in page.html.find(".pkmain", first=True).find(".bordeambos", first=True).find("img"):
        new_pokemon["type"].append(img.attrs["alt"])

    # Extract the Pokemon attacks
    new_pokemon["attacks"] = []
    for attack_item in page.html.find(".pkmain")[-1].find("tr .check3"):
        # Define the attack properties
        attack = {"name": attack_item.find("td", first=True).find("a", first=True).text,
                "type": attack_item.find("td")[1].find("img", first=True).attrs["alt"],
                "min_level": attack_item.find("th", first=True).text,
                "damage": int(attack_item.find("td")[3].text.replace("--", "0"))}
        # Add the attack to the attacks list
        new_pokemon["attacks"].append(attack)
    # Return the new Pokemon data
    return new_pokemon


# Function to get all Pokemon data and save it in a pickle file
def get_all_pokemons():
    # Try to load the Pokemon data from a local file
    try:
        print("Cargando el archivo de pokemons...")
        with open(pokefile_path, "rb") as pokefile:
            all_pokemons = pickle.load(pokefile)
    # If the file is not found, download the data from the internet
    except FileNotFoundError:
        print("¡Archivo no encontrado!, descargando de internet...")

        all_pokemons = []
        total = 151 # Set the total number of pokemon to the game
        bar_length = 30 # Set the length of the progress bar

        for index in range(total):
            all_pokemons.append(get_pokemon(index + 1))

            # Calculate and display the number of '#' characters for the progress bar
            progress = (index + 1) / total
            block = int(round(bar_length * progress))
            text = "\r{0:.0f}% [{1}]".format(progress * 100, '#' * block + '-' * (bar_length - block))
            sys.stdout.write(text)
            sys.stdout.flush()

        # Save the downloaded data to a local file
        with open(pokefile_path, "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)
            print("\n¡Todos los pokemons se han descargado!")
    print("Lista de pokemons cargada exitosamente.")
    # Return the list of all Pokemon
    return all_pokemons


def main():
    pass


if __name__ == "__main__":
    main()