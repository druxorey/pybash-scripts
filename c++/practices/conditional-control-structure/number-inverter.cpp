#include <iostream>

using namespace std;

int main(){
    int originalNumber, invertedNumber = 0;

    cout << endl << "[========= NUMBER INVERTER =========]" << endl << endl;

    cout << "Enter a 5 digit number: "; 
    cin >> originalNumber;

    int one,two,three,four,five;

    one = originalNumber / 10000;
    two = (originalNumber % 10000) / 1000;
    three = (originalNumber % 1000) / 100;
    four = (originalNumber % 100) /10;
    five = originalNumber % 10;

    invertedNumber = (five * 10000)+(four * 1000)+(three * 100)+(two * 10)+ one;        
    
    cout << "The result of inverting the number is: " << invertedNumber << endl;

    return 0;
}

