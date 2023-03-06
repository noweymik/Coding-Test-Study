// Baekjoon Q.4153
// 직각삼각형
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // while문으로 입력받기 (마지막이 0 0 0)
    
    while(true) {
        vector<int> len;
        int n;
        for(int i=0; i<3; i++) {
            cin >> n;
            len.push_back(n);
        }
        if(len[0] == 0 && len[1] == 0 && len[2] == 0) {
            break;
        }
        sort(len.begin(), len.end());
        if(pow(len[2],2) == pow(len[0],2) + pow(len[1],2)) {
            cout << "right\n"; 
        }
        else cout << "wrong\n";
    }

    
    return 0;
}
