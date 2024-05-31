#include <iostream>
#include <cmath>

using namespace std;

int main() {
    float quadraticTerm, linearTerm, constantTerm, discriminantValue, rootValue, finalPositiveValue, finalNegativeValue;

    cout << endl << "[====== SECOND DEGREE POLYNOMAL CALCULATOR ======]" << endl << endl;

    cout << "Enter the quadratic term: ";
    cin >> quadraticTerm; 
    cout << "Enter the linear term: ";
    cin >> linearTerm; 
    cout << "Enter the constant term: ";
    cin >> constantTerm; 
    cout << endl;

    discriminantValue = (pow(linearTerm, 2)) - (4 * quadraticTerm * constantTerm);
    
    if (discriminantValue < 0) {
        cout << "The given polynomial has no real solution" << endl;
        return 0;

    } else {
        rootValue = sqrt(discriminantValue);
        
        finalPositiveValue = ((-1 * linearTerm) + rootValue) / (2 * quadraticTerm);
        finalNegativeValue = ((-1 * linearTerm) - rootValue) / (2 * quadraticTerm);
        
        if (finalPositiveValue < 1 and finalPositiveValue > -1) {
            cout << "The positive value of the polynomial is: " << 0 << endl;
        } else {
            cout << "The positive value of the polynomial is: " << finalPositiveValue << endl;
        }

        if (rootValue != 0) {
            cout << "The negative value of the polynomial is: " << finalNegativeValue << endl;
        }
    }

    return 0;
}

