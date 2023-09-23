print('Bienvenido a la mejor calculadora del planeta tierra')
print('')

x = int(input('Ingresa el primer número: '))
y = int(input('Ingresa el segundo número: '))

operation = (input(
    '''¿Qué operación deseas realizar?: 

    1) Suma
    2) Resta
    3) Multiplicación
    4) División

    Escribe el número de la operación: '''))

if operation == '1':
    print('El resultado es: ', x+y)

elif operation == '2':
    print('El resultado es: ', x-y)

elif operation == '3':
    print('El resultado es: ', x*y)

elif operation == '4':
    print('El resultado es: ', x/y)

else :
    print('Hubo un error, intente nuevamente')
