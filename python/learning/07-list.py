print("Programa lista de compra")

log_out = False
shopping_list = []

while log_out != True:

    item = str(input("¿Que quieres comprar? ([Q] para salir): "))
    
    if item == "Q" or item == "q":
        log_out = True
    elif (item in shopping_list) == True:
        print("Ese item ya se encuentra en la lista de compras")
    else:
        confirmation = input(f"¿Seguro que quieres añadir '{item}' a la lista? [S/N]: ")
        if confirmation in ["S","s"]:
            shopping_list.append(item)                
            print(f"Se ha añadido {item} a la lista")
        else:
            print(f"No se ha añadido '{item}' a la lista")

if len(shopping_list) == 0:
    print("La lista está vacía.")
else:
    print(f"Tu lista de la compra es: {shopping_list}")
