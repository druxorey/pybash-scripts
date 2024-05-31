#include <iostream>
#include <cmath>

using namespace std;

int main(){
    float hourHand, minuteHand, hourAngle, minuteAngle, finalAngle;
     
    cout << endl << "[========= CLOCK HAND'S ANGLE =========]" << endl << endl;

    cout << "Enter the clock hour hand: ";
    cin >> hourHand;
    cout << "Enter the clock minute hand: ";
    cin >> minuteHand;

    hourAngle = hourHand * 30;
    minuteAngle = minuteHand * 6;
    finalAngle = abs((hourAngle + (minuteAngle / 12)) - minuteAngle);

    cout << "The angle between both hand's is: " << finalAngle << endl;

    return 0;
}
