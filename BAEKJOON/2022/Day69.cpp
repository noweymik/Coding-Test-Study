// Baekjoon Q.11948
// 과목선택
#include <iostream>
using namespace std;

int main() {  
    int score, min = 100, sum = 0;
    for(int i=0; i<4; i++) {
        cin >> score;

        if(score < min) {
            min = score;
        }
        sum += score;
    }
    sum -= min; // 물화생지 중 최소 점수 빼기
    min = 100;  // 최솟값 초기화

    for(int i=0; i<2; i++) {
        cin >> score;
        
        if(score < min) {
            min = score;
        }
        sum += score;
    }
    sum -= min; // 역사, 지리 중 최소 점수 빼기
    cout << sum;
}