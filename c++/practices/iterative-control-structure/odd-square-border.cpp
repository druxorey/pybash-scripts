#include <iostream>

using namespace std;

int main(){
    int squarePattern, borderSize;

    cout << endl << "[========= ODD SQUARE BORDER =========]" << endl << endl;

    cout << "1- Chess.\n2- Dots.\n3- Fractal.\n" << endl;
    cout << "Select the square pattern: ";
    cin >> squarePattern;
    
    do {
        cout << "Enter the border size [odd number]: ";
        cin >> borderSize;
    } while (borderSize % 2 == 0);
    
    cout << endl;

    if (squarePattern == 1){

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

    } else if (squarePattern == 2) {

        for (int i = 0; i < borderSize; i++) {

            for (int j = 0; j < borderSize; j++) {
                if (i == 0 || j == 0 || i == borderSize - 1 || j == borderSize - 1) {
                    cout << " x";
                } else if (i % 2 == 0 && j % 2 == 0) {
                    cout << " o";
                } else {
                    cout << "  ";
                }
            }     
            cout << endl;
        }

    } else if (squarePattern == 3) {

        for (int i = 0; i < borderSize; i++) {
            int yDistance = abs(i - (borderSize - 1) / 2);

            for (int j = 0; j < borderSize; j++) {
                int xDistance = abs(j - (borderSize - 1) / 2);

                if (i == 0 || j == 0 || i == borderSize - 1 || j == borderSize - 1) {
                    cout << " x";
                } else if ((yDistance % 2 == 0 && yDistance >= xDistance) || (xDistance % 2 == 0 && xDistance >= yDistance)){
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
