#! /bin/bash

variable="Esta es una cadena de texto"
echo $variable

COLOR="\e[1;35m"
END="\e[0m"
echo -e "$COLOR$variable$END"

numero_1="5"
numero_2="30"
(( numero_3=numero_1+numero_2 ))
echo $numero_3
