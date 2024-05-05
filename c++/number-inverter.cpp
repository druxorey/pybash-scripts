#include <iostream>

using namespace std;

int main(){

    int num, result = 0;

    cout << "Enter a 4 digit number: "; 
    cin >> num;

    int one,two,three,four;

    one = num / 1000;
    two = (num % 1000) / 100;
    three = (num % 100) / 10;
    four = num % 10;

    result = (four * 1000)+(three * 100)+(two * 10)+ one;        

    cout << "The result of inverting the number is: " << result << endl;

    return 0;
}

