x = (input("Escriba su primer número: "))
y = (input("Escriba su segundo número: "))
    
if x < y:
    print(x, 'es menor que', y)
    print(x, 'no es igual a', y)
    print(x, 'es menor o igual a', y) 
    
elif x <= y: 
    print(x, 'es igual a', y)  
    print(x, 'es menor o igual a', y)  
    print(x, 'es mayor o igual a', y) 
    
if x > y:
    print(x, 'es mayor que', y)
    print(x, 'no es igual a', y)
    print(x, 'es mayor o igual a', y) 