// Baekjoon Q.5543
// 상근날드
#include <iostream>
using namespace std;

int main() {  
    int burger[3];
    int drink[2];
    int minB = 2000, minD = 2000; // 가장 저렴한 버거와 드링크 가격

    for(int i=0; i<3; i++) {
        cin >> burger[i];
        if(burger[i] < minB) minB = burger[i];
    }
    for(int i=0; i<2; i++) {
        cin >> drink[i];
        if(drink[i] < minD) minD = drink[i];
    }

    cout << minB + minD - 50;
}