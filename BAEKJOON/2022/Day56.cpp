// Baekjoon Q.1943
// 최소공배수
#include <iostream>
using namespace std;

int gcd(int a, int b) {

    while(b != 0) {
        int N = a % b;
        a = b;
        b = N;
    }
    return a;
}

int main() {     
    int A, B;
    int N;
    cin >> N;

    for(int i=0; i<N; i++) {
        cin >> A >> B;
        cout << (A*B)/gcd(A, B) << endl;
    }   
}
