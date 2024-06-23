#include <iostream>
#include "rand-array.cpp"

using namespace std;

void oddAndEven(int numberList[], int size, int &even, int &odd) {
    even = 0, odd =0;
    for (int i = 0; i < size; i++) {
        if (numberList[i] % 2 == 0) { even ++; }
        else { odd ++; }
    }
}

int main(){
    int size, even, odd;

    printf("\n[========= ODD AND EVEN IN ARRAY =========]\n\n");

    printf("Enter the size of the array: ");
    cin >> size;

    int numberList[size];
    randArray(numberList, size);
    oddAndEven(numberList, size, even, odd);

    printf("In the array are %i odd numbers and %i even numbers.\n", odd, even);

    return 0;
}
