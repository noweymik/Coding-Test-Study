// Baekjoon Q.10872
// 팩토리얼
#include <iostream>
using namespace std;
int calc(int n) {    
    if(n > 0) {
        return n * calc(n-1);
    }
    else {
        return 1;
    }
}
int main() {     
    int n;
    cin >> n;
    cout << calc(n);
    return 0;
}