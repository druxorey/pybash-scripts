print("Introduce a continuación 3 números distintos: ")

first = int(input("Primer número: "))
second = int(input("Segundo número: "))
third = int(input("Tercero número: "))

max_num = max(first,second,third)
min_num = min(first,second,third)

print("Entre los 3 números el mayor es: {}".format(max_num)) 
print("Entre los 3 números el menor es: ", min_num) 
