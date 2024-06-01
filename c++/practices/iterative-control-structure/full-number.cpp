#include <iostream>

using namespace std;

int main() {
    bool isEnded = true;
    int inputNumber, fullNumber = 0;

    cout << endl << "[========= FULL NUMBER =========]" << endl << endl;
    do {
        cout << "Enter the number: ";
        cin >> inputNumber;

        if (inputNumber == -1) {
            isEnded = false;
        } else if (inputNumber < 0 || inputNumber > 10) {
            cout << "That's not acceptable, try again.." << endl;
        } else {
            fullNumber = (fullNumber * 10) + inputNumber;
        }

    } while (isEnded != false);

    cout << fullNumber << endl;

    return 0;
}
