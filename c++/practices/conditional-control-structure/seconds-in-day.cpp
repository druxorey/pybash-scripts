#include <iostream>

using namespace std;

int main(){
    int secondsInDay, minutesInDay, hoursInDay, totalSeconds;
    char meridianData;

    cout << endl << "[========= SECONDS IN A DAY =========]" << endl << endl;

    cout << "Enter the seconds: ";
    cin >> secondsInDay;
    cout << "Enter the minutes: ";
    cin >> minutesInDay;
    cout << "Enter the hours: ";
    cin >> hoursInDay;
    cout << "It's [A]M or [P]M?: ";
    cin >> meridianData;

    if (meridianData == 'P' or meridianData == 'p'){
        hoursInDay += 12;
    }

    totalSeconds = ( secondsInDay + (minutesInDay * 60) + (hoursInDay * 3600) );

    cout << "It's has transcurred " << totalSeconds << " seconds today." << endl;
    
    return 0;
}
