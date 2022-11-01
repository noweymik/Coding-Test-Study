// Baekjoon Q.1546
// 평균
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;   // N : 과목의 개수
    float s, M = 0, total = 0; // s : 점수, M : 최댓값, total : 총점(점수 수정된 상태)    
    vector<float> score;

    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> s;
        if(s > M) M = s;
        score.push_back(s);
    }

    for(auto x : score) {
        x = x/M *100;
        total += x;
    }

    printf("%f", total/(float)N);    
    return 0;
}