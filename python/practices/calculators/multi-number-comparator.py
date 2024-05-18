print("""Bienvenido al comparador de cifras, qué operación quiere realizar?: 

    1) Mayor y menor entre 3 cantidades
    2) Mayor y menor entre 2 cantidades""")

choise = int(input(f"\nEscribe tu opción: "))

if choise == 1:

    print("Introduce a continuación 3 números distintos: ")

    first = int(input("Primer número: "))
    second = int(input("Segundo número: "))
    third = int(input("Tercero número: "))

    max_num = max(first,second,third)
    min_num = min(first,second,third)

    print("Entre los 3 números el mayor es: {}".format(max_num)) 
    print("Entre los 3 números el menor es: ", min_num) 
    exit()

elif choise == 2:
    x = (input("Escriba su primer número: "))
    y = (input("Escriba su segundo número: "))
    
    if x == y:
        print(x, 'es igual a', y)
    
    else:
        print(x, 'no es igual que', y)
        if x > y:
            print(x, 'es mayor que', y)
        elif x < y:
            print(x ,'es menor que', y)
