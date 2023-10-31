// Baekjoon Q.10870
// 피보나치 수 5
#include <iostream>
using namespace std;
int fibonacci (int num);

int main() {   
    int n, Fn;  
    cin >> n;
    Fn = fibonacci(n);
    cout << Fn;
    return 0;
}

int fibonacci (int num) {
    if(num == 0) {
        return 0;
    }
    else if(num == 1) {
        return 1;
    }
    else {
        return fibonacci(num-2) + fibonacci(num-1);
    }
}
