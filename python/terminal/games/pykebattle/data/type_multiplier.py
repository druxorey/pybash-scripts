def multiplier_for_type(first_poke, second_poke):
    type_effectiveness = {
        "normal": {"lucha": 0.5},
        "lucha": {"volador": 0.5, "psiquico": 0.5, "normal": 1.5},
        "fuego": {"agua": 0.5, "roca": 0.5, "tierra": 0.5, "planta": 1.5, "hielo": 1.5, "bicho": 1.5, "acero": 1.5},
        "agua": {"planta": 0.5, "electrico": 0.5, "fuego": 1.5, "tierra": 1.5, "roca": 1.5},
        "planta": {"fuego": 0.5, "hielo": 0.5, "veneno": 0.5, "volador": 0.5, "bicho": 0.5, "tierra": 1.5, "roca": 1.5, "agua": 1.5},
        "electrico": {"tierra": 0.5, "agua": 1.5, "volador": 1.5},
        "hielo": {"fuego": 0.5, "lucha": 0.5, "roca": 0.5, "acero": 0.5, "planta": 1.5, "dragon": 1.5, "tierra": 1.5, "volador": 1.5},
        "veneno": {"tierra": 0.5, "psiquico": 0.5, "planta": 1.5, "hada": 1.5},
        "tierra": {"agua": 0.5, "planta": 0.5, "hielo": 0.5, "fuego": 1.5, "electrico": 1.5, "veneno": 1.5, "roca": 1.5, "acero": 1.5},
        "volador": {"electrico": 0.5, "hielo": 0.5, "roca": 0.5, "bicho": 1.5, "planta": 1.5, "lucha": 1.5},
        "psiquico": {"bicho": 0.5, "fantasma": 0.5, "siniestro": 0.5, "lucha": 1.5, "veneno": 1.5},
        "bicho": {"volador": 0.5, "roca": 0.5, "fuego": 0.5, "siniestro": 1.5, "planta": 1.5},
        "roca": {"agua": 0.5, "planta": 0.5, "lucha": 0.5, "tierra": 0.5, "acero": 0.5, "bicho": 1.5, "volador": 1.5, "hielo": 1.5, "fuego": 1.5},
        "fantasma": {"siniestro": 0.5, "normal": 0.5, "psiquico": 1.5, "fantasma": 1.5},
        "dragon": {"hielo": 0.5, "hada": 0.5, "dragon": 1.5},
        "siniestro": {"lucha": 0.5, "bicho": 0.5, "hada": 0.5, "fantasma": 1.5, "psiquico": 1.5},
        "acero": {"fuego": 0.5, "lucha": 0.5, "tierra": 0.5, "hada": 1.5, "roca": 1.5, "hielo": 1.5},
        "hada": {"veneno": 0.5, "hada": 0.5, "siniestro": 1.5, "dragon": 1.5, "lucha": 1.5}
    }
    total_effectiveness = 0
    for first_type in first_poke["type"]:
        for second_type in second_poke["type"]:
            total_effectiveness += type_effectiveness.get(first_type, {}).get(second_type, 1)
    average_effectiveness = total_effectiveness / (len(first_poke["type"]) * len(second_poke["type"]))
    return average_effectiveness