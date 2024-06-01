#include <iostream>

using namespace std;

int main(){
    long long int iteration = 1, iterationLimit, xNumber = 0, yNumber = 1, auxiliarNumber = 0;

    cout << endl << "[========= FIBONACCI SEQUENCE =========]" << endl << endl;

    cout << "Enter de final position in the fibonaccci sequence: ";
    cin >> iterationLimit;

    do {
        cout << yNumber << endl;
        
        auxiliarNumber = xNumber;
        xNumber = yNumber;
        yNumber = auxiliarNumber + yNumber;
        iteration++;

    } while (iteration != iterationLimit);

    cout << yNumber << endl;

    return 0;
}
