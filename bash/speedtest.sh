#!/bin/bash

function main(){

    start=$(date +%s%N)

    count=0
    number=50000000

    for (( i=0; i<=number; i++ )); do
       true 
    done

    end=$(date +%s%N)
    time=$(( (end - start) / 1000000 ))

    echo "Counting to number $number in Bash took $time ms."
}

main bash
