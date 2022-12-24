// Baekjoon Q.10156
// 과자
#include <iostream>
using namespace std;

int main() {  
    int K, N, M;
    int money;

    cin >> K >> N >> M;
    if(M > K*N) { // 충분한 돈이 있을 때
        cout << 0;
    }
    else {        // 돈이 부족할 때
        cout << K*N - M;
    }
}