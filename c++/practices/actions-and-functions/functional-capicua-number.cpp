#include <iostream>

using namespace std;

bool isCapicua(int number) {
    int capicua = 0, comparator = number;
    do {
        capicua = capicua * 10 + number % 10;
        number /= 10;
    } while (number - 1 != -1);
    return capicua == comparator;
}


int main(){
    int number;

    cout << endl << "[========= FUNCTIONAL CAPICUA NUMBER =========]" << endl << endl;

    do {
        cin.clear();
        printf("Enter the number to be evaluated: ");
        cin >> number;
    } while (!(number < 1000000 && number > 100000));

    for (int i=0; i<=3; i++) {
        int evaluatedNumber = number % 1000;
        if (isCapicua(evaluatedNumber)) {
            printf("The number %i is capicua.\n", evaluatedNumber);
            return 0;
        }
        number /= 10;
    }
    printf("There isn't any capicua number.\n");

    return 0;
}
