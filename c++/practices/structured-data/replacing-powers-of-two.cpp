#include <iostream>
#include <cmath>
#include "array-functions.cpp"

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
    int sizeArray, replacedNumber;
    
    printf("\n[========= REPLACING POWERS OF TWO =========]\n\n");

    printf("Enter the size of the array: ");
    cin >> sizeArray;
    printf("Enter the number: ");
    cin >> replacedNumber;

    int array[sizeArray];

    randArray(array, sizeArray);
    replaceInArray(array, sizeArray, replacedNumber);
    printArray(array, sizeArray);

    return 0;
}
