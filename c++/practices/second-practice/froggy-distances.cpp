#include <iostream>

using namespace std;

int main(){
    int joseJumps, pedroJumps, joseTimes, totalDistance, totalPene;

    cout << endl << "Jose and Pedro are two frogs. Jose can jump a number of centimeters and Pedro can jump a number of centimeters. Assuming that both frogs start jumping at the same point (and in the same direction), will the frogs coincide at the same point at some point before Jose makes a certain number of jumps?" << endl << endl;

    cout << "Enter the distance Jose can jump: ";
    cin >> joseJumps;

    cout << "Enter the times Jose will jump: ";
    cin >> joseTimes;

    cout << "Enter the distance Pedro can jump: ";
    cin >> pedroJumps;
    cout << endl;

    totalDistance = pedroJumps * joseTimes;

    if ((totalDistance % joseJumps) == 0){
        cout << "The frogs will meet at the same point at some point before Jose finishes all his jumps." << endl;
    } else{
        cout << "The frogs will not meet at the same point at some point before Jose finishes all his jumps." << endl;
    }

    return 0;
}
