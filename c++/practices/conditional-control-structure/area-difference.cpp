#include <iostream>

using namespace std;

int main(){
    float baseValue, heightValue, radiusValue, triangleArea, circleArea;

    cout << endl << "[========= AREA DIFFERENCE =========]" << endl << endl;

    cout << "Enter the triangle base value: ";
    cin >> baseValue;
    cout << "Enter the triangle height value: ";
    cin >> heightValue;
    cout << "Enter the circle raius value: ";
    cin >> radiusValue;

    triangleArea = (baseValue * heightValue)/2;
    circleArea = (3.14*(radiusValue * radiusValue));

    cout << endl << "The area of the triangle is: " << triangleArea << endl;
    cout << "The area of the circle is: " << circleArea << endl;
    
    if (circleArea > triangleArea){
        cout << "The circle area is bigger than the triangle area" << endl;
    } else if (circleArea < triangleArea){
        cout << "The triangle area is bigger than the circle area" << endl;
    } else{
        cout << endl << "The circle area and the triangle area are equal" << endl;
    }

    return 0;
}
