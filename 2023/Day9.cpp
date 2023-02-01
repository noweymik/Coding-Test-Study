// Baekjoon Q.5585
// 거스름돈
#include <iostream>
using namespace std;

int main() {
    int c, p, count=0; // c : change, p : price
    cin >> p;
    c = 1000 - p;

    while(c > 0) {
        if(c >= 500) {
            count++;
            c -= 500;
        }
        else if(c >= 100) {
            count++;
            c -= 100;
        }
        else if(c >= 50) {
            count++;
            c -= 50;
        }
        else if(c >= 10) {
            count++;
            c -= 10;
        }
        else if(c >= 5) {
            count++;
            c -= 5;
        }
        else if(c >= 1) {
            count++;
            c -= 1;
        }
    }

    cout << count;
    return 0; 
}
