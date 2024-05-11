#include <iostream>
#include <cmath>

using namespace std;

int main(){

    int i=1, j=2;
    float r=2.0;
    bool b=true;

    cout << "a) " << ((i + 2)*r) << endl;
    cout << "b) " << (i/(2+j) <= 5*j/3) << endl;
    cout << "c) " << (11/2) << endl;
    cout << "d) " << (11/(float)2) << endl;
    cout << "e) " << (b && i + j >= j*5 % 3) << endl << endl;

    int a=3, d=4;
    bool c=true;
    
    cout << "a) " << ((a*2 > d) && c) << endl;
    cout << "b) " << (b/2 - 4*a*b/1/2) << endl;
    cout << "c) " << pow(b/2 - 4*a*b,1/2) << endl;
    cout << "d) " << pow(b/(2-4*a)*b,1/2) << endl << endl;

    int x=3, y=7;

    cout << "a) " << (y%x+y/x) << endl;
    cout << "b) " << (y%2+x*2-2/2) << endl;
    cout << "c) " << ((x/2)+(y/2)-4 >= 3+(float)(2*2)/4.0/8.0 ) << endl;
    cout << "d) " << ((15+2*7)+1>10*5-3*5*18%4) << endl;
    cout << "e) " << (2/3+4/2/2-10+pow(100,1/2)) << endl;
    cout << "f) " << (25-100/20+8+15/pow(2,2)+7<165/7+165%7) << endl;
    cout << "g) " << ((4*(8-pow(3,2))+pow(5/3*2,2)/(12/5)*5+12%5)) << endl;
    cout << "h) " << (13%((5-2)*4)-(3*5+2)/pow(3,2) < 3+7*2-4+pow(12,2)) << endl;
    cout << "i) " << ((!(3 > 1) && (2 < 10)) || ((4 > 1) && (1 < 2))) << endl;

    return 0;
}
