#include <iostream>

using namespace std;

int main(){

    int num, result = 0;

    cout << "Enter a 5 digit number: "; 
    cin >> num;

    int one,two,three,four, five;

    one = num / 10000;
    two = (num % 10000) / 1000;
    three = (num % 1000) / 100;
    four = (num % 100) /10;
    five = num % 10;

    result = (five * 10000)+(four * 1000)+(three * 100)+(two * 10)+ one;        
    
    cout << "The result of inverting the number is: " << result << endl;

    return 0;
}

