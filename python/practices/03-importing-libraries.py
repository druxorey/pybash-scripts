import random

expected_number = random.randint(1,10)

user_number = int(input("Elige un número al azar de entre el 1 y el 10: "))

if user_number == expected_number:
    print("!!! Felicidades, el número es correcto !!!")
if user_number > 10 or user_number < 1:
    print("Ese número es inválido")
else:
    print("Lo siento, ese no es el número")
    print("El número ganador era: ", expected_number)
