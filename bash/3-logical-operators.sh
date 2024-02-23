#! /bin/bash

# -gt = Greater than
# -ge = Greater or equal
# -lt = Lower than
# -le = Lower or equal
# -eq = Equal
# -ne = Not equal

echo -n "Escribe un número: "
read numero

if [[ $numero -gt 5 ]]; then
	echo "Tu número es mayor que 5"
else
	echo "Tu número es igual o menor que 5"
fi

# -a = And
# -o = Or

echo -n "Escribe un número entre 1 y 10: "
read numero

if [ $numero -ge 1 -a $numero -le 10 ]; then
	echo "Tu número está en el rango [1,10]"
else
	echo "Tu número no está en el rango [1,10]"
fi

# [[]] = Expresiones regulares, texto
# [] = Operaciones lógicas, números
