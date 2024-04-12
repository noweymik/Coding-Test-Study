// Baekjoon Q.2525
// 오븐 시계
#include <iostream>
using namespace std;

int main() {
    int A, B;   // A: 시, B: 분
    int C;      // C: 요리하는 데 필요한 시간
    cin >> A >> B;
    cin >> C;

    A += C / 60;
    B += C % 60;

    if(B >= 60) {
        B -= 60;
        A ++;
    }    
    if(A >= 24) {
        A -= 24;
    }
    
    cout << A << " " << B;    
    return 0;
}