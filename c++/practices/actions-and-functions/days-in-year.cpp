#include <iostream>

using namespace std;


int daysInYear(int month) {
    int days = 0;
    for (int i=1; i< month; i++) {
        if (i == 2) { days += 28; }
        else {days += (i == 4 || i == 6 || i == 9 || i == 11)? 30: 31;}
    }
    return days;
}


int main(){
    int month;

    printf("\n[========= DAYS IN THE YEAR =========]\n\n");

    do {
        cin.clear();
        printf("Enter the month: ");
        cin >> month;
    } while (month < 1 || month > 12);

    printf("%i days have passed.\n", daysInYear(month));

    return 0;
}
