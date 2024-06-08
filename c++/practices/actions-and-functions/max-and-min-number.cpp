#include <iostream>

using namespace std;


int maxNumber(int number) {
    int digit, max = 0;
    do {
        digit = number % 10;
        number /= 10;
        if (max < digit){
            max = digit;
            }

    } while ((number - 1) != -1);

    return max;
}


int minNumber(int number) {
    int digit, min = 9;
    do {
        digit = number % 10;
        number /= 10;
        if (min > digit){
            min = digit;
            }
    } while ((number - 1) != -1);

    return min;
}


int main(){
    int number;

    cout << endl << "[========= MAX AND MIN NUMBER =========]" << endl << endl;

    do {
        cin.clear();
        printf("Enter the number to be evaluated: ");
        cin >> number;
    } while (!(number < 100000 && number > 10000));

    printf("The max number is %i\n", maxNumber(number));
    printf("The min number is %i\n", minNumber(number));
    return 0;
}
