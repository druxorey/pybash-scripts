#include <iostream>

using namespace std;

int main(){
    int binary = 0, decimal = 0;
    int firstPosition,secondPosition,thirdPosition,fourthPosition;

    cout << endl << "[========= BINARY TO DECIMAL CALCULATOR =========]" << endl << endl;

    cout << "Enter a 4 digit binary number: "; 
    cin >> binary;

    firstPosition = binary / 1000;
    secondPosition = (binary % 1000) / 100;
    thirdPosition = (binary % 100) / 10;
    fourthPosition = binary % 10;

    decimal = (firstPosition * 8) + (secondPosition * 4) + (thirdPosition * 2) + (fourthPosition * 1);

    cout << "The decimal value is: " << decimal << endl;

    return 0;
}
