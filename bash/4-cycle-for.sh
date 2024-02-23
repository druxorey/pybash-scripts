#!/bin/bash

echo -ne "Escribe un número: "
read limite

for (( i = 0; i <= $limite; i++ )); do
	echo $i
done
