import numpy as np

print("""
    ¿Qué operación vas a realizar?
    
    1) Calculadora de coordenadas polares a cartesianas
    2) Calculadora de coordenadas cartesianas a polares
    """)

calculadora = int(input("Elige una opción: "))   

if calculadora == 1: 
    def PolarToCartesian(r, theta):
        theta = np.radians(theta)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        return (x, y)

    r = float(input("Ingrese el valor de r: "))
    theta = float(input("Ingrese el valor de theta: "))

    x, y = PolarToCartesian(r, theta)

    print("Resultado: ", x, y)

elif calculadora == 2: 
    def CartesianToPolar(x, y):
        r = np.hypot(x, y)
        theta = np.degrees(np.arctan2(y, x))
        return (r, theta)

    x = float(input("Ingrese el valor de x: "))
    y = float(input("Ingrese el valor de y: "))

    r, theta = CartesianToPolar(x, y)

    print("Resultado de r: ", r)
    print("Resultado de theta: ", theta)

else:
    print('Error, intente nuevamente')
