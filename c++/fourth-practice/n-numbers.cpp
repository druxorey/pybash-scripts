#include <iostream>

using namespace std;

int main(){
    int inputNumber;
    cout << "Enter the number: ";
    cin >> inputNumber;

    int contadorNumber = 0;
    int i = 0;

    for (i = 0; inputNumber > 0; i++) {
        inputNumber /= 10;
        contadorNumber++;
    }

    cout << "The number has " << contadorNumber << " digits." << endl;
    return 0;
}
