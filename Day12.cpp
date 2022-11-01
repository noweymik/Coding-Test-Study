// Baekjoon Q.1110
// 더하기 사이클
#include <iostream>
using namespace std;

int main() {
    int N, cycle = 0;
    int ori_N, new_N;
    cin >> N;
    ori_N = N;
    
    // 십의 자리 수  : N/10, 일의 자리 수 : N%10
    do {                
        new_N = (N%10) * 10 + (((N/10) + (N%10)) %10);
        N = new_N;
        cycle ++;
    } while(ori_N != new_N);

    cout << cycle;
    return 0;
}