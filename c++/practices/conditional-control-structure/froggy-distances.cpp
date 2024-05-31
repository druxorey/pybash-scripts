#include <iostream>

using namespace std;

int main(){
    int joseDistance, pedroDistance, joseJumps;

    cout << endl << "[========= FROGGY DISTANCES =========]" << endl << endl;

    cout << "Enter the distance Jose can jump: ";
    cin >> joseDistance;
    cout << "Enter the times Jose will jump: ";
    cin >> joseJumps;
    cout << "Enter the distance Pedro can jump: ";
    cin >> pedroDistance;
    cout << endl;

    if ( (joseDistance * pedroDistance) <= (joseDistance * joseJumps) ){
        cout << "The frogs will meet at the same point before Jose finishes all his jumps." << endl;
    } else{
        cout << "The frogs will not meet at some point before Jose finishes all his jumps." << endl;
    }

    return 0;
}
