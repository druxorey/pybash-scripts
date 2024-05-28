#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int hourHand, minuteHand;
    float hourAngle, minuteAngle, finalAngle;
     
    cout << endl << "[========= CLOCK HAND'S ANGLE =========]" << endl << endl;

    cout << "Enter the clock hour hand: ";
    cin >> hourHand;

    cout << "Enter the clock minute hand: ";
    cin >> minuteHand;
    
    if (hourHand % 2 == 0 && minuteHand % 2 == 0) {
        hourAngle = hourHand * 30;
        minuteAngle = minuteHand * 6;
        finalAngle = abs((hourAngle) - minuteAngle);

        cout << "The angle between both hand's is: " << finalAngle << endl;
    } else {
        cout << "Hours: " << hourHand << endl;
        cout << "Minutes: " << minuteHand << endl;
    }

    return 0;
}
