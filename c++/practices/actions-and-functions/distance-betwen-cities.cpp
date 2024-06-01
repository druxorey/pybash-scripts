#include <iostream>

using namespace std;

float milleToKm(int distance) {
    return (float)distance * 1.6;
}

void nextCities() {
    string firstCity, secondCity;
    float initialDistance, finalDistance;
    cout << "Introduce la primera ciudad: ";
    cin >> firstCity;
    cout << "Introduce la segunda ciudad: ";
    cin >> secondCity;
    cout << "Introduce la distancia entre ambas ciudades: ";
    cin >> initialDistance;

    finalDistance = milleToKm(initialDistance);

    cout << "La distancia entre " << firstCity << " y " << secondCity << " es de " << finalDistance << " km." << endl;
}

bool isContinued () {
    char continued;
    cout << "¿Quieres introducir otra ciudad? [Y/N]: ";
    cin >> continued;

    if (continued == 'y' || continued == 'Y') {
        return 1;
    }

    return 0;
}

int main(){
    int distance;

    do {
        nextCities();
    } while (isContinued());

    return 0;
}
