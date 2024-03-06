import pickle

from requests_html import HTMLSession

pokemon_base = {
    "name": "",
    "current_health": 100,
    "base_health": 100,
    "level": 1,
    "type" : None,
    "current_exp": 0,
    "defense": 10,
    "attack" : 10
}

URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="


def get_pokemon(index):
    url = "{}{}".format(URL_BASE, index)
    session = HTMLSession()

    new_poke = pokemon_base.copy()
    pokemon_page = session.get(url)

    pokemon_name_full = (pokemon_page.html.find(".mini", first=True).text).split("\n")[0]
    new_poke["name"] = pokemon_name_full
    print( str(index)+" : "+pokemon_name_full)

    new_poke["type"] = []
    new_poke["attacks"] = []

    for img in pokemon_page.html.find(".pkmain",first=True).find(".bordeambos",first=True).find("img"):
        new_poke["type"].append(img.attrs["alt"])

    for attack_item in  pokemon_page.html.find(".pkmain")[-1].find("tr .check3"):
        attack = {
            "name":attack_item.find("td",first=True).find("a",first=True).text,
            "type":attack_item.find("td")[1].find("img",first=True).attrs["alt"],
            "min_level":attack_item.find("th",first=True).text,
            "damage": int(attack_item.find("td")[3].text.replace("--","0"))
        }

        # Arregla los ataques pokemons con min level vacio ('')
        attack["min_level"].replace("",str(1))

        new_poke["attacks"].append(attack)

    return new_poke


def get_all_poke():
    all_pokemons = []
    try:
        with open("pokefile.pkl","rb") as pokefile:
            all_pokemons= pickle.load(pokefile)
            return all_pokemons
    except FileNotFoundError:
        for index in range(151):
            all_pokemons.append(get_pokemon(index + 1))
        with open("pokefile.pkl", "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)

        return all_pokemons
get_all_poke()