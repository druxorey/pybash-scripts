#include <iostream>
#include "rand-array.cpp"

using namespace std;

void averageInArray(int array[], int size, int number, int &quantity) {
    for (int i = 0; i < size; i++) {
        quantity += (array[i] >= number) ? 1 : 0;
    }
}


int main() {
    int arraySize, averageNumber, quantity = 0;
    
    printf("\n[========= AVERAGE ARRAY ITEM =========]\n\n");

    printf("Enter the size of the array: ");
    cin >> arraySize;
    printf("Enter the averge number: ");
    cin >> averageNumber;

    int array[arraySize];

    randArray(array, arraySize);
    averageInArray(array, arraySize, averageNumber, quantity);

    printf("\nFinal quantity: %i\n", quantity);
    return 0;
}
