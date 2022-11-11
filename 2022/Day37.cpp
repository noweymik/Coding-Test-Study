// Baekjoon Q.2753
// 윤년
#include <iostream>
using namespace std;

int main() {     
    int year;
    cin >> year;
    if(year % 4 == 0 && year % 100 !=0) {   // 윤년
        cout << 1;
    }
    else if(year % 400 == 0) {  // 윤년
        cout << 1;
    }
    else {  // 윤년 아닐 때
        cout << 0;
    }
    return 0;
}