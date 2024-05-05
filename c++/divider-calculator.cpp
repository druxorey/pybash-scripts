#include <iostream>

using namespace std;

int main () {
    int a;
    cout << "Ingrese un número"<< endl; 
    cin >> a ;
    
        if(a > 0){
            cout << "El número ingresado es positivo" << endl;
        } else {
            cout << "El número ingresado es negativo" << endl;
        }
   
    int numerador, denominador;

    cout << "Ingrese el numerador de la división" << endl; 
    cin >> numerador;

    cout << "Ingrese el denominador de la división" << endl; 
    cin >> denominador;

    if(denominador != 0) {
        cout << numerador << "/" << denominador << "=" << numerador/denominador << endl;
    } else {
        cout << "El denominador no puede ser 0" << endl;
    }

    return 0;
}
