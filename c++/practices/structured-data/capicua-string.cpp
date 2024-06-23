#include <iostream>

using namespace std;

bool isCapicua(string text) { 
    int lenght = text.length(); 
    for (int i = 0 ; i <= lenght/2 ; i++) {
        if (text[lenght-1-i] != text[i]) {
            return false;
        }
    }
    return true;
}


int main() {
    string textNormal;

    printf("\n[========= CAPICUA STRING =========]\n\n");

    printf("Enter the string: ");
    cin >> textNormal;

    if (isCapicua(textNormal)) {
        printf("The string is capicua.\n");
    } else {
        printf("The string is not capicua.\n");
    }

    return 0;
}
