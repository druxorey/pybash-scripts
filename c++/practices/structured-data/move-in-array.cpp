#include <iostream>
#include "array-functions.cpp"

using namespace std;

void moveInArray(int array[], int size, int move) {
    int movedArray[size], displace = 0;

    for (int i = 0; i < size; i++) {
        displace = (i - move < 0)? size - (move - i) : i - move ;
        movedArray[displace] = array[i];
    }

    for (int i = 0; i < size; i++) {array[i] = movedArray[i];}
} 


int main() {
    int sizeArray, averageNumber;

    printf("\n[========= MOVE IN ARRAY =========]\n\n");
    
    printf("Enter the size of the array: ");
    cin >> sizeArray;
    printf("Enter the averge number: ");
    cin >> averageNumber;

    int array[sizeArray];

    fillArray(array, sizeArray);
    printArray(array, sizeArray);

    moveInArray(array, sizeArray, averageNumber);
    printArray(array, sizeArray);

    return 0;
}
