from requests_html import HTMLSession
import pickle
import sys
import os

PKBASE = {
    "name": "",
    "current_health": 100,
    "base_health": 100,
    "level": 1,
    "type": None,
    "current_exp": 0,
    "defense": 10,
    "attack" : 10
}

URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="

# Get the path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Join the current directory path with the file name
pokefile_path = os.path.join(current_dir, "pokefile.pkl")


def get_pokemon(index):
    url = "{}{}".format(URL_BASE, index)
    session = HTMLSession()

    new_pokemon = PKBASE.copy()
    page = session.get(url)

    new_pokemon["name"] = page.html.find(".mini", first=True).text.split("\n")[0]
    
    new_pokemon["type"] = []
    for img in page.html.find(".pkmain", first=True).find(".bordeambos", first=True).find("img"):
        new_pokemon["type"].append(img.attrs["alt"])

    new_pokemon["attacks"] = []

    for attack_item in page.html.find(".pkmain")[-1].find("tr .check3"):
        attack = {
            "name": attack_item.find("td", first=True).find("a", first=True).text,
            "type": attack_item.find("td")[1].find("img", first=True).attrs["alt"],
            "min_level": attack_item.find("th", first=True).text,
            "damage": int(attack_item.find("td")[3].text.replace("--", "0")),
        }
        new_pokemon["attacks"].append(attack)
    return new_pokemon


def get_all_pokemons():
    try:
        print("Cargando el archivo de pokemons...")
        with open(pokefile_path, "rb") as pokefile:
            all_pokemons = pickle.load(pokefile)
    except FileNotFoundError:
        print("¡Archivo no encontrado!, descargando de internet...")
        all_pokemons = []
        for index in range(9):
            all_pokemons.append(get_pokemon(index + 1))
            print("*", end="")
            sys.stdout.flush()
        with open(pokefile_path, "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)
            print("\n¡Todos los pokemons se han descargado!")
    print("Lista de pokemons cargada exitosamente.")
    return all_pokemons

def main():
    pass

if __name__ == "__main__":
    main()