#!/bin/bash

# Error function
error() {
    echo $1
    exit 1
}

# Code to detect errors and avoid problems
if [ $# -ne 4 ]; then
    error "Uso: script nombre extensión número ruta"
fi

if [ ! -d $4 ]; then
    error "Error: el directorio no existe"
fi

if [ $3 -lt 1 ]; then
    error "Error: el numero de ficheros no puede ser menor que 1"
fi

# File creator
for (( i = 1; i <= $3; i++ )); do
    name="$4/$1$i.$2"
    if [ $i -lt 10 ]; then
        name="$4/$10$i.$2"
    fi
    touch $name
    echo "Fichero $name creado" | tr -s /
done
