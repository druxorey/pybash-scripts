# Declaración inicial de la variable
respuesta = None

# Bucle while
while respuesta != "A" and respuesta != "B" and respuesta != "C":

    respuesta = input("¿Qué opcion eliges? [A, B o C]: ")
    respuesta = respuesta.upper()

# Cuando sale del bucle se revisan las siguientes condiciones
if respuesta == "A":
    print("Has elegido A")
elif respuesta == "B":
    print("Has elegido B")
elif respuesta == "C":
    print("Has elegido C")

    numero = int(input("Introduce un número: "))

    while numero > 0:
        print("El número es: ", numero)
        numero -= 1
else:
    print("No has elegido nada válido")
