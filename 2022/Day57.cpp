// Baekjoon Q.11050
// 이항 계수 1
#include <iostream>
using namespace std;

int bi_Coefficient (int n, int k) {
    if(k==0 || k==n) {
        return 1;
    }
    else {
        return bi_Coefficient(n-1, k-1) + bi_Coefficient(n-1, k);
    }
}

int main() {     
    int N, K;
    cin >> N >> K;
    cout << bi_Coefficient(N, K);
}
