// Baekjoon Q.2884
// 알람 시계
#include <iostream>
using namespace std;

int main() {     
    int H, M;
    cin >> H >> M;

    if(M >= 45) {       // M이 45 이상일 경우
        M = M - 45;
    }
    else {              // M이 45 미만일 경우
        if(H == 0) {    // H가 0시인 경우, 1시간 전이면 23시
            H = 23;
        }
        else {
            H = H - 1;
        }
        M = 60 - (45 - M);
    }

    cout << H << " " << M;
    return 0;
}
