// Baekjoon Q.1924
// 2007년
#include <iostream>
using namespace std;

int main() {  
    int x, y; // x : month, y : date
    int day = 0;
    int month[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    cin >> x >> y;

    // 총 며칠째인지 구하기
    for(int i=0; i<x-1; i++) {
        day += month[i];
    }
    day += y;

    if(day % 7 == 0) cout << "SUN";
    else if(day % 7 == 1) cout << "MON";
    else if(day % 7 == 2) cout << "TUE";
    else if(day % 7 == 3) cout << "WED";
    else if(day % 7 == 4) cout << "THU";
    else if(day % 7 == 5) cout << "FRI";
    else if(day % 7 == 6) cout << "SAT";

}