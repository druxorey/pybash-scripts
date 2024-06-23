#include <iostream>

using namespace std;

bool isCapicua(string example) { 
    int lenght = example.length(); 
    for (int i = 0 ; i <= lenght/2 ; i++) {
        if (example[lenght-1-i] != example[i]) {
            return false;
        }
    }
    return true;
}


int main(){
    string example;

    printf("\n[========= CAPICUA STRING =========]\n\n");

    printf("Enter the string: ");
    cin >> example;

    if (isCapicua(example)) {
        printf("The string is capicua.\n");
    } else {
        printf("The string is not capicua.\n");
    }

    return 0;
}
