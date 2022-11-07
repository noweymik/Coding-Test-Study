// Baekjoon Q.25305
// 커트라인
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {     
    int N, k, input;
    vector<int> score;

    cin >> N >> k;

    for(int i=0; i<N; i++) {
        cin >> input;
        score.push_back(input);
    }
    sort(score.rbegin(), score.rend()); // 내림차순 정렬
    cout << score[k-1] << endl;
    return 0;
}
