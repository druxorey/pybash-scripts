#include <iostream>

using namespace std;

int main(){
    int inputNumber, i;

    cout << endl << "[========= DIGITS IN A NUMBER =========]" << endl << endl;

    cout << "Enter the number: ";
    cin >> inputNumber;

    for (i = 0; inputNumber > 0; i++) {
        inputNumber /= 10;
    }
    cout << "The number has " << i << " digits." << endl;

    return 0;
}
