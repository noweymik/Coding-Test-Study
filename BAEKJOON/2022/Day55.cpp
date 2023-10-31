// Baekjoon Q.2581
// 소수
#include <iostream>

using namespace std;
bool isPrime(int num);

int main() {     
    int M, N;
    int total = 0, min;    
    bool prime = false;

    cin >> M >> N;
    
    min = N;     
    for(int i=M; i<=N; i++) {
        if(isPrime(i)) {
            total = total + i;
            if(i < min) min = i;
            prime = true;
        }
    }

    if(!prime) {    // 소수가 아예 없을 경우
        cout << -1;
    }
    else {
        cout << total << endl;
        cout << min;
    }
}

bool isPrime(int num) {
    if(num < 2) return false;

    for(int i=2; i*i<=num; i++) {
        if(num % i == 0) return false;
    }

    return true;
}