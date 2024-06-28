#include <iostream>
#include "array-functions.cpp"

using namespace std;

bool isArraySum(int array[], int size, int compared) {
    for (int i = 0; i < size; i++) {
        int firstSum = array[i];
        for (int j = 0; j < size - i; j++) {
            int secondSum = array[j+i];
            if (firstSum + secondSum == compared) {
                return true;
            }
        }
    }
    return false;
}


int main() {
    int finalNumber, sizeArray;

    printf("\n[========= SUMATORY ITEMS IN ARRAY =========]\n\n");

    printf("Enter the array size: ");
    cin >> sizeArray;

    printf("Enter the number to be compared: ");
    cin >> finalNumber;

    int array[sizeArray];
    fillArray(array, sizeArray);

    if (isArraySum(array, sizeArray, finalNumber)) {
        printf("\nIn this array there is 2 numbers that if we add them it gives %i.\n", finalNumber);
    } else {
        printf("\nIn this array there are not 2 numbers that if we add them it gives %i.\n", finalNumber);
    }


    return 0;
}
