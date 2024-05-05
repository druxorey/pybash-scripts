#include <iostream>

using namespace std;

int main(){
    int firstDistance, secondDistance, secondTimes, totalDistance;

    cout << endl << "Jose and Pedro are two frogs. Jose can jump a number of centimeters and Pedro can jump a number of centimeters. Assuming that both frogs start jumping at the same point (and in the same direction), will the frogs coincide at the same point at some point before Joe makes a certain number of jumps?" << endl << endl;

    cout << "Enter the distance Jose can jump: ";
    cin >> firstDistance;

    cout << "Enter the distance Pedro can jump: ";
    cin >> secondDistance;

    cout << "Enter the times Pedro will jump: ";
    cin >> secondTimes;
    cout << endl;

    totalDistance = secondTimes * secondDistance;

    if ((totalDistance % firstDistance) == 0){
        cout << "The frogs will meet at the same point at some point before Jose finishes all his jumps." << endl;
    } else{
        cout << "The frogs will not meet at the same point at some point before Jose finishes all his jumps." << endl;
    }

    return 0;
}
