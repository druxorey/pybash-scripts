#include <iostream>
#include <cmath>

using namespace std;

int main(){
    float firstCathetus, secondCathetus, hypotenuseValue;

    cout << endl << "[========= TRIANGLE HYPOTENUSE CALCULATOR =========]" << endl << endl;

    cout << "Enter the triangle first cathetus value: ";
    cin >> firstCathetus;
    cout << "Enter the triangle second cathetus value: ";
    cin >> secondCathetus;

    hypotenuseValue = sqrt(pow(firstCathetus, 2) + pow(secondCathetus, 2));
    
    cout << endl << "The hypotenuse of that triangle is: " << hypotenuseValue << endl << endl;

    return 0;
}
