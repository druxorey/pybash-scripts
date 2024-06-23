#include <iostream>
#include "rand-array.cpp"

using namespace std;

int maxArray(int array[], int size) {
    int maxNumber = array[0];

    for (int i = 1; i < size; i++) {
        int element = array[i];

        if (element > maxNumber) {
            maxNumber = element;
        }
    }
    return maxNumber;
};

int main(){
    int arraySize;
    int initialArray[arraySize];

    printf("\n[========= MAX ARRAY ITEM =========]\n\n");

    printf("Enter the size of the array: ");
    cin >> arraySize;

    randArray(initialArray, arraySize);
    printf("The max number in the array is %i.\n", maxArray(initialArray, arraySize));

    return 0;
}
