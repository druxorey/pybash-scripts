#include <iostream>

using namespace std;

void moveInArray(int array[], int size, int move) {
    int movedArray[size], displace = 0;

    for (int i = 0; i < size; i++) {
        displace = (i - move < 0)? size - (move - i) : i - move ;
        movedArray[displace] = array[i];
    }

    for (int i = 0; i < size; i++) {array[i] = movedArray[i];}
} 


int main(){
    int arraySize, averageNumber;

    printf("\n[========= MOVE IN ARRAY =========]\n\n");
    
    printf("Enter the size of the array: ");
    cin >> arraySize;
    printf("Enter the averge number: ");
    cin >> averageNumber;
    cout << endl;

    int array[arraySize];

    for (int i = 0; i < arraySize; i++) {
        array[i] = i;
        printf("%i ", array[i]);
    }

    cout << endl;
    moveInArray(array, arraySize, averageNumber);

    for (int i = 0; i < arraySize; i++) {
        printf("%i ", array[i]);
    }

    cout << endl;
    return 0;
}
