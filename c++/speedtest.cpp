#include <iostream>
#include <chrono>

using namespace std;

int main(){
    int count=0, number=50000000;
    auto start = chrono::high_resolution_clock::now();

    for(int i=0; i<=number; i++){
        count += 1;
    }

    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);

    cout << "Counting to number " << number << " in C++ took " << duration.count() << " ms." << endl;

    return 0;
}
