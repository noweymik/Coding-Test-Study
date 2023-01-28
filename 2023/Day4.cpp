// Baekjoon Q.2501 
// 약수 구하기
#include <iostream>

using namespace std;

int main() {
    int n, k;
    int num = 0;
    cin >> n >> k;  
    
    for(int i=1; i<=n; i++) {
        if(n%i == 0) {
            num += 1;
        }
        if(num == k) {
            cout << i;
            return 0;
        }
    }
    cout << 0;
}
