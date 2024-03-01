print("Voy a la cocina")
print("Abro la nevera")

milk_check = input("¿Hay leche en la nevera? (S/N) : ")
toddy_check = input("¿Hay toddy en la nevera? (S/N) : ")

milk_check = milk_check.lower()
toddy_check = toddy_check.lower()

if milk_check != "s" or toddy_check != "s":
    print("Voy al supermercado a comprar: ")
    if milk_check != "s":
        print(" - Leche")
    if toddy_check != "s":
        print(" - Toddy")
else:
    print("Ponemos la leche en el vaso")
    print("Ponemos el toddy en el vaso")
    print("Mezclamos")
