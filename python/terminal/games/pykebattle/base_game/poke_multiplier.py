def set_multiplier_for_type(first_poke, second_poke):
    first_type = first_poke["type"][0]
    second_type = second_poke["type"][0]

    if first_type == "normal" and second_type == "lucha":
        return 0.5
    elif first_type == "lucha":
        if second_type == "volador" or second_type =="psiquico":
            return 0.5
        if second_type == "normal":
            return 1.5
    elif first_type == "fuego":
        if second_type == "agua" or second_type =="roca" or second_type =="tierra":
            return 0.5
        if second_type == "planta" or second_type =="hielo" or second_type =="bicho" or second_type =="acero":
            return 1.5
    elif first_type == "agua":
        if second_type == "planta" or second_type =="electrico":
            return 0.5
        if second_type == "fuego" or second_type =="tierra" or second_type =="roca":
            return 1.5
    elif first_type == "planta":
        if second_type == "fuego" or second_type =="hielo" or second_type =="veneno" or second_type =="volador" or second_type =="bicho":
            return 0.5
        if second_type == "tierra" or second_type =="roca" or second_type =="agua":
            return 1.5
    elif first_type == "electrico":
        if second_type == "tierra":
            return 0.5
        if second_type == "agua" or second_type =="volador":
            return 1.5
    elif first_type == "hielo":
        if second_type == "fuego" or second_type =="lucha" or second_type =="roca" or second_type =="acero":
            return 0.5
        if second_type == "planta" or second_type =="dragon" or second_type =="tierra" or second_type =="volador":
            return 1.5
    elif first_type == "veneno":
        if second_type == "tierra" or second_type =="psiquico":
            return 0.5
        if second_type == "planta" or second_type =="hada":
            return 1.5
    elif first_type == "tierra":
        if second_type == "agua" or second_type =="planta" or second_type =="hielo":
            return 0.5
        if second_type == "fuego" or second_type =="electrico" or second_type =="veneno" or second_type =="roca" or second_type =="acero":
            return 1.5
    elif first_type == "volador":
        if second_type == "electrico" or second_type =="hielo" or second_type =="roca":
            return 0.5
        if second_type == "bicho" or second_type =="planta" or second_type =="lucha":
            return 1.5
    elif first_type == "psiquico":
        if second_type == "bicho" or second_type =="fantasma" or second_type =="siniestro":
            return 0.5
        if second_type == "lucha" or second_type =="veneno":
            return 1.5
    elif first_type == "bicho":
        if second_type == "volador" or second_type =="roca" or second_type =="fuego":
            return 0.5
        if second_type == "siniestro" or second_type =="planta":
            return 1.5
    elif first_type == "roca":
        if second_type == "agua" or second_type =="planta" or second_type =="lucha" or second_type =="tierra" or second_type =="acero":
            return 0.5
        if second_type == "bicho" or second_type =="volador" or second_type =="hielo" or second_type =="fuego":
            return 1.5
    elif first_type == "fantasma":
        if second_type == "siniestro" or second_type =="normal":
            return 0.5
        if second_type == "psiquico" or second_type =="fantasma":
            return 1.5
    elif first_type == "dragon":
        if second_type == "hielo" or second_type =="hada":
            return 0.5
        if second_type == "dragon":
            return 1.5
    elif first_type == "siniestro":
        if second_type == "lucha" or second_type =="bicho" or second_type =="hada":
            return 0.5
        if second_type == "fantasma" or second_type =="psiquico":
            return 1.5
    elif first_type == "acero":
        if second_type == "fuego" or second_type =="lucha" or second_type =="tierra":
            return 0.5
        if second_type == "hada" or second_type =="roca" or second_type =="hielo":
            return 1.5
    elif first_type == "hada":
        if second_type == "veneno" or second_type =="hada":
            return 0.5
        if second_type == "siniestro" or second_type =="dragon" or second_type =="lucha":
            return 1.5
    return 1
