print("Programa número más pequeño")

choise = int(input("¿Que forma de hacerlo quieres probar? [1,2,3,4]: "))

if choise == 1:
    number_list = []

    while True:
        number = input("Añade un número a la lista [Q para salir]: ")
    
        if number == "q" or number == "Q":
            break
        elif int(number) in number_list:
            print("Ese número ya se encuentra en la lista")
        elif number not in number_list:
            number = int(number)
            number_list.append(number)                
            print(f"Se ha añadido {number} a la lista")

    if len(number_list) == 0:
        print("La lista está vacía.")
    else:
        max_number = max(number_list)
        min_number = min(number_list)

        print(f"De entre los siguientes números: {number_list}")
        print(f"El número más grande es {max_number}")
        print(f"El número más pequeño es {min_number}")

if choise == 2:
    number_list = []
    number_inserted = int(input("Introduzca un número a la lista: "))
    number_list.append(number_inserted)

    while input("¿Desea introducir más números? [S/N]: ") == "s":
        number_inserted = int(input("Introduzca un número a la lista: "))
        number_list.append(number_inserted)

    min_number = number_list[0]
    max_number = number_list[0]

    for number in number_list[1:]:
        if min_number > number:
            min_number = number
        if max_number < number:
            max_number = number

    print("Número grande: {}, Número pequeño: {}".format(max_number,min_number))
if choise == 3:
    number_inserted = input("Introduzca los números separados por coma: ")
    number_list = number_inserted.split(",")
    number_int = []

    for number in number_list: 
        number_int.append(int(number))

    min_number = number_list[0]
    max_number = number_list[0]

    for number in number_list[1:]:
        if min_number > number:
            min_number = number
        if max_number < number:
            max_number = number

    print("Número grande: {}, Número pequeño: {}".format(max_number,min_number))
if choise == 4:

    number_inserted = input("Introduzca los números separados por coma: ")
    number_list = [int(number) for number in number_inserted.split(",")]

    min_number = number_list[0]
    max_number = number_list[0]

    for number in number_list[1:]:
        if min_number > number:
            min_number = number
        if max_number < number:
            max_number = number

    print("Número grande: {}, Número pequeño: {}".format(max_number,min_number))
