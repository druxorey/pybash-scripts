#include <iostream>

using namespace std;

int main(){
    float productPrice, ivaValue, finalProductValue;

    cout << endl << "[========= IVA CALCULATOR =========]" << endl << endl;

    cout << "Enter the product price: ";
    cin >> productPrice;

    ivaValue = productPrice * 0.12;
    finalProductValue = ivaValue + productPrice;

    cout << endl << "The product IVA value is: " << ivaValue << endl;
    cout << "The final product value is: " << finalProductValue << endl;

    return 0;
}
