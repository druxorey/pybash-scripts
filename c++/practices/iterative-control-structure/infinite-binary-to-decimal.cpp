#include <iostream>

using namespace std;

int main(){

    int binary, correctedBinary = 0, iteration = 1, decimal = 0, finalDecimal = 0;

    cout << endl << "[========= INFINITE BINATY TO DECIMAL =========]" << endl << endl;

    do {
        cout << "Enter the number: ";
        cin >> binary;

        if (binary == 1 || binary == 0){
            correctedBinary = correctedBinary * 10 + binary;
        } else if (binary != -1){
            cout << "Wrong number" << endl;
        }
    } while (binary != -1);

    cout << endl << "The binary number is : " << correctedBinary << endl;

    for (int i = 1; correctedBinary > 0; i*=2) {
        decimal = (correctedBinary % 10) * i;
        correctedBinary /= 10;
        finalDecimal += decimal;  
    }

    cout << "The decimal number is: " << finalDecimal << endl;

    return 0;
}
