import sys
import numpy as np

def myReadNumber(mystr):
     mystr2 = f'Ingresa el {mystr} (y presiona return/enter): '
     var = 0
     while var < 3:
        try:
            x = input(mystr2)
            x = float(x)
            return x
        except:
            print (f"Ingresaste: {x}")
            print ("Ese No fue un número válido. Intenta de nuevo.")
            var = var + 1
            print(f'Ese fue intento {var} de 3')

            print('\t Todos los intentos fueron incorrectos. Programa finalizado ')
     sys.exit()

r = myReadNumber("radio")
tethain = myReadNumber("ángulo en grados")

def PolarToCartisian(r, tethain):
    tethain = np.radians(tethain)
    x = r * np.cos(tethain)
    y = r * np.sin(tethain)
    return (x, y)

x, y = PolarToCartisian(r, tethain)

print("Resultado: ", x, y)