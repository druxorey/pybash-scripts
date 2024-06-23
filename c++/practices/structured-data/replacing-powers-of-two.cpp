#include <iostream>
#include <cmath>
#include "rand-array.cpp"

using namespace std;

void replaceInArray(int array[], int size, int number) {
    int i = 0, position = 0;
    do {
        position = pow(2,i) - 1;
        array[position] = number;
        i++;
    } while (pow(2,i) < size - 1);
}


int main(){
    int arraySize, replacedNumber;
    
    printf("\n[========= REPLACING POWERS OF TWO =========]\n\n");

    printf("Enter the size of the array: ");
    cin >> arraySize;
    printf("Enter the number: ");
    cin >> replacedNumber;

    int array[arraySize];

    randArray(array, arraySize);
    replaceInArray(array, arraySize, replacedNumber);
    cout << endl;

    for (int i = 0; i < arraySize; i++) {
        printf("%i ", array[i]);
    }

    return 0;
}
