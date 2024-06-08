#include <iostream>

using namespace std;

bool isInHeight (int yVertex, int yPoint, int height) {
    return (yPoint >= (yVertex - height) && yPoint <= yVertex);
}


bool isInWidth (int xVertex, int xPoint, int width) {
    return (xPoint <= (xVertex + width) && xPoint >= xVertex);
}


int main(){
    int xPoint, yPoint, xVertex, yVertex, height, width; 

    printf("\n[========= POINT IN RECTANGLE =========]\n\n");

    printf("Enter the x and y position: ");
    cin >> xPoint >> yPoint;
    printf("Enter the x and y vertex position: ");
    cin >> xVertex >> yVertex;
    printf("Enter the height: ");
    cin >> height;
    printf("Enter the width: ");
    cin >> width;

    bool heightValue = isInHeight(yVertex, yPoint, height);
    bool widthValue = isInWidth(xVertex, xPoint, width);

    if (heightValue && widthValue) {
        printf("The point is in the rectangle.\n");
    } else {
        printf("The point is not in the rectangle.\n");
    }
    return 0;
}
