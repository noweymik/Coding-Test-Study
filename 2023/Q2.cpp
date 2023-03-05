// Baekjoon Q.25628 
// 햄버거 만들기
#include <iostream>

using namespace std;

int main() {
    int A, B;
    cin >> A >> B;

    if(A/2 == B) cout << B;
    else if(A/2 < B) cout << A/2;
    else cout << B;
    return 0;
}