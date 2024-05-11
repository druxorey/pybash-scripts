#include <iostream>

using namespace std;

int main(){
    int initialHour, finalHour, totalHour;
    float firstHour, extraHour;
    
    cout << endl << "[========= CLOCK HAND'S ANGLE =========]" << endl << endl;

    cout << "Enter the initial hour: ";
    cin >> initialHour;

    cout << "Enter the final hour: ";
    cin >> finalHour;

    totalHour = finalHour - initialHour;

    if (totalHour <= 1){
        cout << "sexo" << 100 << endl;
    } else {
        cout << "En un total de " << totalHour << " horas, acumulaste una deuda de: " << ((80 * (totalHour - 1)) + 100) << endl;
    }

    return 0;
}
