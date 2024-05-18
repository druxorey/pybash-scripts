import string

exercise = int(input("¿Qué ejercicio quiere realizar? [1,2,3]: "))

if exercise == 1:

    spaces = 0
    dots = 0
    commas = 0

    user_text = str(input("Escribe una frase: "))

    for letter in user_text:
        if letter == " ":
            spaces += 1
        elif letter == ".":
            dots += 1
        elif letter == ",":
            commas += 1

    print(f"He encontrado {spaces} espacios")
    print(f"He encontrado {dots} puntos")
    print(f"He encontrado {commas} comas")

elif exercise == 2:

    user_text = input("Introduzca un texto: ")

    upper_letters = 0

    for letter in user_text:
        if letter in string.ascii_uppercase:
            upper_letters += 1

    print("Se han encontrado {} letras en mayúsculas".format(upper_letters))

elif exercise == 3:

    number = int(input("Introduce un número: "))
    
    multiplication_list = range(1,101)

    for i in multiplication_list:
        multiplication_result = number * i
        print(f"{number} x {i} = {multiplication_result}")

