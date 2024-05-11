#include <iostream>

using namespace std;

int main(){
    float distance, time, speed;
    
    cout << endl << "[========= SPEED CALCULATOR =========]" << endl << endl;

    cout << "Introduce the distance in meters: ";
    cin >> distance;

    cout << "Introduce the time in seconds: ";
    cin >> time;

    speed = distance * time;

    cout << "The speed is: " << speed << " m/s." << endl;

    return 0;
}
