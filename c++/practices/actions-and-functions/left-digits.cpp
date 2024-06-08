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

    cout << endl << "[========= LEFT DIGITS =========]" << endl << endl;

    cout << "Enter the number: ";
    cin >> fullNumber;
    cout << "Enter the final number: ";
    cin >> stop;

    cout << "The final calculation is: " << extractDigits(invertNumber(fullNumber), stop) << endl;
    return 0;
}
