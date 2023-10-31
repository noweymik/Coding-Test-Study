// Baekjoon Q.3003
// 킹, 퀸, 룩, 비숍, 나이트, 폰
#include <iostream>
using namespace std;

int main() {     
    int piece[6] = {1, 1, 2, 2, 2, 8};
    int input[6] = {0};
    
    for(int i=0; i<6; i++) {
        cin >> input[i];
    }
    for(int j=0; j<6; j++) {
        cout << piece[j] - input[j] << " ";
    }
    return 0;
}