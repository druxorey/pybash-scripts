#include <iostream>

using namespace std;

int main(){
    int initialHour, initialMinutes, finalHour, finalMinutes, totalMinutes, displayedHours, displayedMinutes;
    float basicAmount = 80, extraAmount = 100, totalPayment;
    
    cout << endl << "[========= PARKING PAYMENT =========]" << endl << endl;

    cout << "Enter the initial hour: ";
    cin >> initialHour;
    cout << "Enter the initial minutes: ";
    cin >> initialMinutes;
    cout << endl;

    cout << "Enter the final hour: ";
    cin >> finalHour;
    cout << "Enter the final minutes: ";
    cin >> finalMinutes;
    cout << endl;
    
    totalMinutes = (finalHour * 60 + finalMinutes) - (initialHour * 60 + initialMinutes);

    if (totalMinutes <= 60 and totalMinutes > 0){
        totalPayment = (float)totalMinutes * 100 / 60;
        cout << "You delayed " << totalMinutes << " minutes. The amount to be paid is a total of Bs." << totalPayment << endl;

    } else{
        if (totalMinutes <= 0){totalMinutes = 24 * 60 - abs(totalMinutes);}
        
        totalPayment = (((float)totalMinutes - 60) * 80 / 60) + 100;
        displayedHours = totalMinutes / 60;
        displayedMinutes = totalMinutes % 60; 

        cout << "You delayed " << displayedHours << " hours and " << displayedMinutes << " minutes. The amount to be paid is a total of Bs." << totalPayment << endl;

    }

    return 0;
}
