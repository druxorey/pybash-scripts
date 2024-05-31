#include <iostream>

using namespace std;

int main() {
	int firstNumber, secondNumber, thirdNumber;
	int firstX, firstY, secondX, secondY, thirdX, thirdY;
	int xFinal, yFinal;

	cout << "Enter the first number: ";
	cin >> firstNumber;
	cout << "Enter the second number: ";
	cin >> secondNumber;
	cout << "Enter the third number: ";
	cin >> thirdNumber;

	firstX = firstNumber / 100;
	firstY = firstNumber % 100;

	secondX = secondNumber / 100;
	secondY = secondNumber % 100;

	thirdX = thirdNumber / 100;
	thirdY = thirdNumber % 100;

	xFinal = (firstX + secondX + thirdX) / 3;
	yFinal = (firstY + secondY + thirdY) / 3;

	cout << "The final coordinate is X:" << xFinal << " Y:" << yFinal << endl;

	return 0;
}
