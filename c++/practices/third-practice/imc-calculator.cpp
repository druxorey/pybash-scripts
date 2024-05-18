#include <iostream>
#include <cmath>

using namespace std;

int main(){
    float height = 0, weight = 0, imc = 0, conversion = 0.453592;
    
    cout << endl << "[========= IMC CALCULATOR =========]" << endl << endl;

    cout << "Enter your weight in pounds: ";
    cin >> weight;
    cout << "Enter your height in centimeters: ";
    cin >> height;
    cout << endl;

    weight = weight * conversion;
    height = height / 100;

    imc = weight / pow(height, 2);

    cout << weight << "kg -> " << imc << " -> ";

    if (imc < 16) {cout << "Entry criteria" << endl;}
    else if (imc >= 16 && imc < 17) {cout << "Underweight" << endl;}
    else if (imc >= 17 && imc < 18.5) {cout << "Under weight" << endl;}
    else if (imc >= 18.5 && imc < 25) {cout << "Normal weight" << endl;}
    else if (imc >= 25 && imc < 30) {cout << "Over weight" << endl;}
    else if (imc >= 30 && imc < 35) {cout << "Premorbid obesity" << endl;}
    else if (imc >= 40 && imc <= 45) {cout << "Morbid obesity" << endl;}
    else {cout << "Hypermorbid obesity" << endl;}

    return 0;
}
