#include <iostream>

using namespace std;


int invertNumber (int fullNumber) {
    int invertedNumber = 0;
    do {
        invertedNumber = (invertedNumber * 10) + (fullNumber % 10);
        fullNumber /= 10;
    } while ((fullNumber -1) != -1);
    return invertedNumber;
}


int extractDigits(int fullNumber, int stop) {
    bool isEnded = false;
    int finalQuantity = 0;
    do {
        if (fullNumber % 10 == stop) {
            isEnded = true;
        } else {
            finalQuantity = (finalQuantity * 10) + (fullNumber % 10);
            fullNumber /= 10;
        }
    } while (!isEnded);
    return finalQuantity;
}


int main(){
    int fullNumber, stop;

    cout << "Ingresa los dígitos: ";
    cin >> fullNumber;
    cout << "Ingresa el punto de parada: ";
    cin >> stop;

    cout << "El cálculo final es: " << extractDigits(invertNumber(fullNumber), stop) << endl;
    return 0;
}
