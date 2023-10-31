// Baekjoon Q.2747
// 피보나치 수
#include <iostream>
using namespace std;

int main() {  
    int N;
    long long list[45];

    cin >> N;

    list[0] = 0;
    list[1] = 1;

    for(int i=2; i<=N; i++) {
        list[i] = list[i-1] + list[i-2];
    }
    cout << list[N];
}