#include <iostream>

using namespace std;

int main(){
    int squareType;

    cout << "Select the square type: ";
    cin >> squareType;

    if (squareType == 1){
        int borderSize;

        cout << endl << "[========= ODD SQUARE BORDER =========]" << endl << endl;

        cout << "Enter the border size: ";
        cin >> borderSize;
        cout << endl;

        for (int i = 0; i < borderSize; i++) {

            for (int j = 0; j < borderSize; j++) {
                if (i % 2 == 0 || i == borderSize - 1 || j % 2 == 0 || j == borderSize - 1) {
                    cout << " x";
                } else {
                    cout << "  ";
                }
            }     
            cout << endl;
        }
    } else if (squareType == 2) {
        int borderSize;

        cout << endl << "[========= ODD SQUARE BORDER =========]" << endl << endl;

        cout << "Enter the border size: ";
        cin >> borderSize;
        cout << endl;

        for (int i = 0; i < borderSize; i++) {

            for (int j = 0; j < borderSize; j++) {
                if (i == 0 ||
                    j == 0 || 
                    i == borderSize - 1 || 
                    j == borderSize - 1) {
                    cout << " x";
                } else if (
                    ((i % 2 == 0 && j % 2 == 0)) ||
                    ((i % 2 == 0 && j % 2 == 0))
                        ) {
                    cout << " o";
                } else {
                    cout << "  ";
                }
            }     
            cout << endl;
        }


    } 

    return 0;
}
