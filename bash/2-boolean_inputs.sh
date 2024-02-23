#! /bin/bash

echo -n "Escribe algo: "
read mensaje
echo "Tu mensaje es el siguiente: $mensaje"

echo -n "Esta es una pregunta, responde si o no: [s/n]"
read resultado

if [[ $resultado == "s" ]]; then
	echo "Respondiste que si"
elif [[ $resultado == "n" ]]; then
	echo "Respondiste que no"
else
	echo "Respondiste algo fuera de los parámetros"
fi
