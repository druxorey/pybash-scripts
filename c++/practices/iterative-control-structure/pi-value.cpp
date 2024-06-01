#include <iostream>

using namespace std;

int main(){
    
    double inputNumber, piValue = 4;

    cout << endl << "[========= PI VALUE =========]" << endl << endl;

    cout << "Enter the number of iterations: ";
    cin >> inputNumber;

    for (double i = 3; i <= (inputNumber * 4) ; i += 4) {
        piValue = piValue - (4/i) + (4/(i+2));
    }
    
    cout << "The value of pi is: " << piValue << endl;
    
    return 0;
}
