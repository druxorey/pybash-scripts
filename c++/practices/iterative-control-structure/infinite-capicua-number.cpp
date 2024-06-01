#include <iostream>

using namespace std;

int main() {
    int inputNumber;

    cout << endl << "[========= INFINITE CAPICUA NUMBER =========]" << endl << endl;

    cout << "Enter the number: ";
    cin >> inputNumber;

    int capicuaNumber = 0;
    int temporalNumber = inputNumber;

    for (int i = 0; temporalNumber > 0; i++) {
        capicuaNumber = capicuaNumber * 10 + temporalNumber % 10;
        temporalNumber = temporalNumber / 10;
    }
    
    if (capicuaNumber == inputNumber) {
        cout << "The number " << inputNumber << " is capicua." << endl;
    } else {
        cout << "The number " << inputNumber << " is not capicua." << endl;
    }

    return 0;
}
