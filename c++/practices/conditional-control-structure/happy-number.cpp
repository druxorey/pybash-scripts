#include <iostream>

using namespace std;

int main(){
    int initialNumber, one, two, three, four;
    bool isHappyNumber = false, isAscendantNumber = false;

    cout << endl << "[========= HAPPY NUMBER =========]" << endl << endl;

    cout << "Enter a 4 digit nummber: ";
    cin >> initialNumber;

    one = initialNumber / 1000;
    two = (initialNumber % 1000) / 100;
    three = (initialNumber % 100) / 10;
    four = initialNumber % 10;

    isHappyNumber = initialNumber / 100 > initialNumber % 100;
    isAscendantNumber = four > three && three > two && two > one;

    cout << "The number is ";
    if (isHappyNumber && isAscendantNumber)
        cout << "very happy." << endl;
    else if (!isHappyNumber && !isAscendantNumber)
        cout << "unhappy." << endl;
    else if (isAscendantNumber)
        cout << "ascendant." << endl;
    else if (isHappyNumber)
        cout << "happy." << endl;
    return 0;
}
