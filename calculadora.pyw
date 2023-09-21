from tkinter import *

raiz = Tk()
raiz.title("Calculadora de Cociente y Residuo")
raiz.iconbitmap("folder-apps.ico")
raiz.config(bg="#b1b5bd")
raiz.mainloop()


dividendo = input("Ingrese el dividendo: ")
divisor = input("Ingrese el divisor: ")

if dividendo == "Messi" and divisor == "Dios":
    print("Efectivamente, Messi es el mejor del mundo")
if divisor == "0":
    print("El divisor no puede ser 0")
else:
    try:
        dividendo = float(dividendo)
        divisor = float(divisor)
        cociente = dividendo // divisor
        residuo = dividendo % divisor

        print(
            f"El cociente de dividir {dividendo} entre {divisor} es: ", cociente)
        print(
            f"El residuo de dividir {dividendo} entre {divisor} es: ", residuo)

    except:
        print("Hubo un error, intente nuevamente")
