#!/bin/bash

function help() {
    echo
    echo "USAGE: touches [FILES NAME] [FILES QUANTITY] [FILES ROUTE]"
    echo
    echo "DESCRIPTION: Creates a default file in a specific programming language."
    echo
    echo "ARGUMENTS:"
    echo "  FILE TYPE: bash, c++, python, rust."
    echo "  FILE NAME: (Optional) The name of the file."
    echo
    echo "EXAMPLES:"
    echo "  defaultfi c++ helloWorld"
    echo "  defaultfi python"
    echo
    echo "Report bugs to https://github.com/druxorey/pybash-scripts/issues"
    echo
    exit 1
}

function main () {

    if [ $# -ne 3 ]; then
        help
    fi

    if [ ! -d $3 ]; then
        error "Error: el directorio no existe"
    fi

    if [ $2 -lt 1 ]; then
        error "Error: el numero de ficheros no puede ser menor que 1"
    fi

    name=$($1 | cut -d'.' -f1)
    extension=$($1 | cut -d'.' -f2)

    for (( i = 1; i <= $2; i++ )); do
        file="$3/$name-$i.$extension"
        if [ $i -lt 10 ]; then
            file="$3/$name-0$i.$extension"
        fi
        echo $file
        echo "Fichero $file creado" | tr -s /
    done
    }

main $@
