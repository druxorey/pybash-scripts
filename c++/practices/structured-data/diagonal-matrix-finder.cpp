#include <iostream>

using namespace std;


void fillMatrix(int** matrix, int sizeMatrix) {
    int nose = 1;
    for (int i = 0; i < sizeMatrix; i++) {
        for (int j = 0; j < sizeMatrix; j++) {
            matrix[i][j] = nose + j;
            if (nose + j < 10) {cout << " ";}
            cout << nose + j << "|";
        }
        nose += sizeMatrix;
        cout << endl;
    }
}


int diagonalMatrix(int** matrix, int sizeMatrix) {
    int finalSum = 0;
    for (int i = 0; i < sizeMatrix; i++) {
        finalSum += matrix[i][(sizeMatrix - 1) - i];
    }
    return finalSum;
}


int main() {
    int sizeMatrix;

    printf("\n[========= DIAGON MATRIX FINDER =========]\n\n");

    printf("Enter the size of the array: ");
    cin >> sizeMatrix;

    int** matrix = new int*[sizeMatrix]; 
    for (int i = 0; i < sizeMatrix; i++) {
        matrix[i] = new int[sizeMatrix];
    }

    fillMatrix(matrix, sizeMatrix);
    cout << diagonalMatrix(matrix, sizeMatrix) << endl;
    
    for (int i = 0; i < sizeMatrix; i++) {
        delete[] matrix[i]; 
    }
    delete[] matrix; 

    return 0;
}
