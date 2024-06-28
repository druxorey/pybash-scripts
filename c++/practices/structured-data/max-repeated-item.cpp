#include <iostream>
#include "array-functions.cpp"

using namespace std;

int repeatedItem(int array[], int size) {
    int maxValue = array[0], maxRepeated = 1;

    for (int i = 0; i < size; i++) {
        int evaluatedRepeated = 0, evaluatedValue = array[i];;

        for (int j = 0; j < size - i ; j++) {
            if (evaluatedValue == array[j]) {evaluatedRepeated ++;}
        } 

        if (maxRepeated < evaluatedRepeated) {
            maxValue = evaluatedValue;
            maxRepeated = evaluatedRepeated;
        }
    }
    return maxValue;
}


int main() {
    int sizeArray;
    printf("\n[========= MAX REPEATED ITEM =========]\n\n");

    cout << "Enter the size of the array: ";
    cin >> sizeArray;
    int array[sizeArray];

    randArray(array, sizeArray);
    printArray(array, sizeArray);

    printf("\nThe most repeated value is %i.\n", repeatedItem(array, sizeArray));

    return 0;
}
