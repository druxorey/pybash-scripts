#include <iostream>

using namespace std;

int main(){
    float m1, b1, m2, b2, xIntersection, yIntersection;

    cout << endl << "[========= INTERSECTION OF NON-PARALLEL LINES =========]" << endl << endl;

    cout << "Introduce the incline for the first line: ";
    cin >> m1;
    cout << "Introduce the indepentent term for the first line: ";
    cin >> b1;

    cout << "Introduce the incline for the second line: ";
    cin >> m2;
    cout << "Introduce the indepentent term for the second line: ";
    cin >> b2;

    xIntersection = (b2-b1)/(m1-m2);
    yIntersection = m1*(b2-b1)/(m1-m2)+b1;

    cout << "The intersection is: (" << xIntersection << "," << yIntersection << ")" << endl;

    return 0;
}
