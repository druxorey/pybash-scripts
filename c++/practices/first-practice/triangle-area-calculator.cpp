#include <iostream>

using namespace std;

int main(){
    float baseValue, heightValue, areaValue;

    cout << endl << "[========= TRIANGLE AREA CALCULATOR =========]" << endl << endl;

    cout << "Enter the triangle base value: ";
    cin >> baseValue;

    cout << "Enter the triangle height value: ";
    cin >> heightValue;

    areaValue = (baseValue * heightValue)/2;

    cout << endl << "The area of that triangle is: " << areaValue << endl << endl;

    return 0;
}
