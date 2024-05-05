#include <iostream>

using namespace std;

int main(){

    int num, result = 0;
    int firstPosition,secondPosition,thirdPosition,fourthPosition;

    cout << "Enter a 4 digit number: "; 
    cin >> num;

    firstPosition = num / 1000;
    secondPosition = (num % 1000) / 100;
    thirdPosition = (num % 100) / 10;
    fourthPosition = num % 10;

    result = (firstPosition * 8) + (secondPosition * 4) + (thirdPosition * 2) + (fourthPosition * 1);

    cout << "The decimal value of this number is: " << result << endl;

    return 0;
}
