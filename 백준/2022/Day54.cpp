// Baekjoon Q.1978
// 소수 찾기
#include <iostream>

using namespace std;
bool isPrime(int num);

int main() {     
    int N, num;
    int prime_number = 0;

    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> num;
        if(isPrime(num)) {
            prime_number++;
        }
    }

    cout << prime_number;
    return 0;
}

bool isPrime(int num) {
    if(num < 2) return false;

    for(int i=2; i*i<=num; i++) {
        if(num % i == 0) return false;
    }

    return true;
}