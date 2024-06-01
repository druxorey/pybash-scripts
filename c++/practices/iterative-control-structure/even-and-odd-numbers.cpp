#include <iostream>

using namespace std;

int main(){
    int number, iteration = 0, evenNumbers = 0, oddNumbers = 0, totalNumbers = 0;

    cout << endl << "[========= EVEN AND ODD NUMBERS =========]" << endl << endl;
    
    do {
        cout << "Enter the number: ";
        cin >> number;
        
        totalNumbers += number;
        iteration++;

        if (number % 2 == 0) {
            oddNumbers += number;
        } else {
            evenNumbers += number;
        }

    } while (number != 0);

    float oddPercentage, evenPercentage;

    oddPercentage = ((float)oddNumbers / totalNumbers) * 100;
    evenPercentage = ((float)evenNumbers / totalNumbers) * 100;

    cout << endl;
    cout << "The sum of all odd numbers is: " << oddNumbers << endl;
    cout << "The percentage of all even numbers is: " << oddPercentage << "%" << endl;
    cout << "The sum of all even numbers is: " << evenNumbers << endl;
    cout << "The percentage of all even numbers is: " << evenPercentage << "%" << endl;
    cout << "The sum of all numbers is: " << totalNumbers << endl;
    cout << "You enter a total of " << iteration << " numbers."<< endl;

    return 0;
}
