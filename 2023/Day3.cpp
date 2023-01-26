// Baekjoon Q.5691 
// 평균 중앙값 문제
#include <iostream>

using namespace std;

int main() {
    int A, B, C;
    int num;

    while(1) {
        cin >> A >> B;
        if(A == 0 && B == 0) break;
        // (A + B + C) / 3 == A
        C = 3*A - (A+B);
        cout << C << endl;
    }

    return 0;
}
