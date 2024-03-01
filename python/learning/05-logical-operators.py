age = int(input("¿Cuál es tu edad?: "))
carnet = str(input("¿Qué tipo de carnet tienes? (E, P, F, N): "))

carnet = carnet.lower()

if (25 <= age <= 35 and carnet == "e") or (age <= 10) or (age >= 65 and carnet == "p") or (carnet == "f"):
    print("sexo")
else:
    print("nosexo")
