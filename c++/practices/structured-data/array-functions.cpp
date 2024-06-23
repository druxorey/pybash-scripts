#include <iostream>

using namespace std;

int randArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        array[i] = rand() % size;
    }
    return array[size];
}

int fillArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        array[i] = i;
    }
    return array[size];
}

void printArray(int array[], int size) {
    cout << endl;
    for (int i = 0; i < size; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}
