#include <iostream>
#include <string>
#include <sstream> 

using namespace std;

int main() {
    string initialSentence, token, firstWord, nosequeco;
    int iteration = 0, length;
    printf("\n[========= STRING FUNCTION =========]\n\n");

    printf("Enter the string: ");
    getline(cin, initialSentence, '\n');

    istringstream iss(initialSentence);
    nosequeco = initialSentence;

    while (getline(iss, token, ' ')) {
        if (iteration == 0) {
            firstWord = token;
            length = firstWord.length();
            for (int i = 0; i < length; i++) {
                nosequeco[length+i] += firstWord[length-1-i];
            }
        }
        cout << endl << iteration << " " << token;
        iteration++;
    }
    cout << endl << "La oración eliminando espacios es: " << nosequeco << endl;

    printf("\n\nTotal words in the sentence: %i\n", iteration);

    string invertedSentence;
    length = initialSentence.length();
    for (int i = 0; i < length; i++) {
       invertedSentence += initialSentence[length-1-i];
    }

    cout << "La oración invertida es: " << invertedSentence << endl;

    string invertedString;
    length = firstWord.length();

    for (int i = 0; i < length; i++) {
        invertedString += firstWord[length-1-i];
    }

    cout << "La primera palabra es: " << firstWord << endl;
    cout << "La primera palabra invertida es: " << invertedString << endl;

    char temporal;
    printf("Enter the string: ");
    getline(cin, initialSentence, '\n');
    printf("Enter the char: ");
    cin >> temporal;

    istringstream oss(initialSentence);


    iteration = 0;
    while (getline(oss, token, ' ')) {
        length = initialSentence.length();
        for (int i = 0; i < length; i++) {
            if (token[i] == temporal) {
                token[i] += token[+i];
            }
        }
        cout << endl << iteration << " " << token;
        iteration++;
    }
    cout << endl << "La oración eliminando espacios es: " << token << endl;


    return 0;
}
