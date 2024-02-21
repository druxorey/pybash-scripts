score = 0

print("Bienvenido al test para saber cuánto te gusta YSY A")

name = str(input("Por favor introduce tu nombre: "))

print("""
    Pregunta 1: ¿Cuál es el número del diablo?

    A) 666
    B) 247
    C) 616
""")

answer1 = str(input("Responde la letra de la opción que creas correcta: "))
answer1 = answer1.lower()
if answer1 == "a" or answer1 == "c":
    score += 0
elif answer1 == "b":
    score += 10

print("Tu puntaje actual es: ", score)

print("""
    Pregunta 2: ¿Cuál es el mejor disco del YSY?

    A) ANTENAZA 247
    B) HECHO A MANO
    C) YSYSMO
    D) EL AFTER DEL AFTER
    E) Todos los anteriores
""")

answer2 = str(input("Responde la letra de la opción que creas correcta: "))
answer2 = answer2.lower()
if answer2 == "a" or answer2 == "b" or answer2 == "c" or answer2 == "d":
    score += 5
elif answer2 == "e":
    score += 10

print("Tu puntaje actual es: ", score)

print("""
    Pregunta 3: ¿Cómo se llama su hijo?

    A) ysychiquito
    B) todos los cantantes de la industria
    C) Bruno
""")

answer3 = str(input("Responde la letra de la opción que creas correcta: "))
answer3 = answer3.lower()
if answer3 == "a":
    score += 0
elif answer3 == "b":
    score += 5
elif answer3 == "c":
    score += 10

print(f"Muy bien {name} tu puntuación final es: {score}")

if score == 30:
    print("ERES EL VERDADERO FAN DEL YSY A")
elif 5 < score < 30:
    print("Está bien, te gusta YSY")
elif score <= 5:
    print("Fan por moda")
