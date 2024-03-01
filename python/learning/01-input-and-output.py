print("Introduce a continuación 3 números distintos: ")

first = int(input("Primer número: "))
second = int(input("Segundo número: "))
third = int(input("Tercero número: "))

max_num = max(first,second,third)
min_num = min(first,second,third)

print("Entre los números {}, {} y {}".format(first,second,third))
print("El mayor es: ", max_num) 
print("El menor es: ", min_num) 
