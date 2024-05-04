#include <iostream>
#include <cmath>

using namespace std;

int main(){

    float quadraticTerm, linearTerm, constantTerm, discriminantValue, rootValue, finalPositiveValue, finalNegativeValue;

    cout << endl << "[========= CALCULADORA DE LA RESOLVENTE =========]" << endl << endl;

    cout << "Ingresa el término cuadrático: ";
    cin >> quadraticTerm; 
    cout << "Ingresa el término lineal: ";
    cin >> linearTerm; 
    cout << "Ingresa el término constante: ";
    cin >> constantTerm; 
    cout << endl;

    discriminantValue = (pow(linearTerm, 2)) - (4 * quadraticTerm * constantTerm);
    
    if (discriminantValue < 0){
        cout << "El polinomio dado no tiene una solución real" << endl;
        return 0;
    } else {
        rootValue = sqrt(discriminantValue);
        
        finalPositiveValue = ((-1 * linearTerm) + rootValue) / (2 * quadraticTerm);
        finalNegativeValue = ((-1 * linearTerm) - rootValue) / (2 * quadraticTerm);
        
        if (finalPositiveValue < 1 and finalPositiveValue > -1){
            cout << "El valor positivo del polinomio es: " << 0 << endl;
        } else {
            cout << "El valor positivo del polinomio es: " << finalPositiveValue << endl;

        }

        if (rootValue != 0){
            cout << "El valor negativo del polinomio es: " << finalNegativeValue << endl;
        }
    }

    return 0;
}

