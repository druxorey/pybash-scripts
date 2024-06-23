#include <iostream>
#include "array-functions.cpp"

using namespace std;

void oddAndEven(int numberList[], int size, int &even, int &odd) {
    even = 0, odd =0;
    for (int i = 0; i < size; i++) {
        if (numberList[i] % 2 == 0) { even ++; }
        else { odd ++; }
    }
}

int main(){
    int sizeArray, evenQuantity, oddQuantity;

    printf("\n[========= ODD AND EVEN IN ARRAY =========]\n\n");

    printf("Enter the size of the array: ");
    cin >> sizeArray;

    int numberList[sizeArray];
    randArray(numberList, sizeArray);
    oddAndEven(numberList, sizeArray, evenQuantity, oddQuantity);

    printf("In the array are %i odd numbers and %i even numbers.\n", oddQuantity, evenQuantity);

    return 0;
}
