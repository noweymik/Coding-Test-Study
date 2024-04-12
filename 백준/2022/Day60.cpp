// Baekjoon Q.2576
// 홀수
#include <iostream>
using namespace std;

int main() {  
    int n;
    int min = 100, total = 0;   
    for(int i=0; i<7; i++) {
        cin >> n;
        if(n%2!=0) {
            total += n;
            if(n < min) min = n;
        }
    }
    if(total == 0) { // 홀수가 없었을 경우
        cout << -1;
    }
    else {
        cout << total << endl;
        cout << min;
    }
}

