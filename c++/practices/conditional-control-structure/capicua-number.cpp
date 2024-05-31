#include <iostream>

using namespace std;

int main(){
    int inputNumber, outputNumber;
     
    cout << endl << "[========= CAPICUA NUMBER =========]" << endl << endl;

    cout << "Enter the number: ";
    cin >> inputNumber;

    outputNumber = ((inputNumber % 10) * 10000)+(((inputNumber % 100) /10) * 1000)+(((inputNumber % 1000) / 100) * 100)+(((inputNumber % 10000) / 1000) * 10)+ (inputNumber / 10000); 

    if (inputNumber == outputNumber){
        cout << endl << "The number is capicua" << endl;
    } else{
        cout << endl << "The number is not capicua" << endl;
    }

    return 0;
}
