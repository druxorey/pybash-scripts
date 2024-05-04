#include <iostream>

using namespace std;

int main(){

    int num, result = 0;

    cout << "Ingresa un número de 4 cifras: "; 
    cin >> num;

    int one,two,three,four;

    one = num / 1000;
    two = (num % 1000) / 100;
    three = (num % 100) / 10;
    four = num % 10;

    result = (four * 1000)+(three * 100)+(two * 10)+ one;        

    cout << "El resultado de invertir el número es: " << result << endl;

    return 0;
}

