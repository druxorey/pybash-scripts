#include <iostream>

using namespace std;

int main(){
    int borderSize;

    cout << endl << "[========= SQUARE BORDER =========]" << endl << endl;

    cout << "Enter the border size: ";
    cin >> borderSize;

    for (int i = 0; i < borderSize; i++) {

        for (int j = 0; j < borderSize; j++) {
            if (i == 0 || i == borderSize - 1 || j == 0 || j == borderSize - 1) {
                cout << " x";
            } else {
                cout << "  ";
            }
        }     
        cout << endl;
    }

    return 0;
}
