print("Bienvenido, acá sabrás que teléfono es el indicado para tí")

phone_election = "Ninguno"

print("""¿Qué sistema operativo prefieres?
    
    1) IOS
    2) Android
""")

os_election = int(input("Elige en número de la opción que veas correcta: "))

if os_election == 1:
    print("¿Tienes dinero? [S/N]: ")
    money_election = str(input("Elige la opción que veas correcta: "))

    if money_election == "S" or money_election == "s":
         phone_election = "Iphone Ultra Pro Max Special Edition Fornai 3000"

    elif money_election == "N" or money_election == "n":
         phone_election = "Iphone 2"

elif os_election == 2:
    print("¿Tienes dinero? [S/N]: ")
    money_election = str(input("Elige la opción que veas correcta: "))

    if money_election == "S" or money_election == "s":
            
        print("¿Quieres un teléfono gamer? [S/N]: ")
        gamer_election = str(input("Elige la opción que veas correcta: "))

        if gamer_election == "S" or gamer_election == "s":
             phone_election = "Redmagick"

        elif gamer_election == "N" or gamer_election == "n":
             phone_election = "Pixel Pro Google 9000"

    elif money_election == "N" or money_election == "n":
         phone_election = "Chayomi"

print("Tu teléfono ideal es un " + phone_election)
