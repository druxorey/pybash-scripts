#include <iostream>

int randArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        array[i] = rand() % size;
    }
    return array[size];
}
