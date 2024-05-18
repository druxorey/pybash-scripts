import math

character = [] 
start, end = 0,1
isPalindromo = None

string = (str(input("Ingresa un texto: ")))

for i in string.lower():
    character.append(i)

for j in character:
    if character[start] == character[(start - end)]:
        end += 2
        start += 1
    else:
        isPalindromo = True
        break

if isPalindromo:
    print("El texto no es un palindromo")
else:
    print("El texto es un palindromo")

