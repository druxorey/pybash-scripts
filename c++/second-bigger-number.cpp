#include <iostream>

using namespace std;

int main(){
    int firstNumber, secondsNumber;

    cout << endl << "[========= SECOND BIGGEST NUMBER =========]" << endl << endl;

    cout << "Enter the first number: ";
    cin >> firstNumber;

    cout << "Enter the second number: ";
    cin >> secondsNumber;

    if (firstNumber < secondsNumber){
        cout << endl << "The first number is the second biggest" << endl;
    } else{
        cout << endl << "The second number is the second biggest" << endl;
    }

    return 0;
}
