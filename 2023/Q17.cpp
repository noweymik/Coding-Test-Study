// Baekjoon Q.2822
// 점수 계산
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, total = 0;
    vector<int> v1;
    vector<int> v2;
    vector<int> idx;

    for(int i=0; i<8; i++) {
        cin >> N;
        v1.push_back(N);
    }
    v2 = v1;
    sort(v2.rbegin(), v2.rend());

    for(int i=0; i<5; i++) {
        total += v2[i];
        for(int k=0; k<8; k++) {
            if(v2[i] == v1[k]) {
                idx.push_back(k+1);
            }
        }
    }
    cout << total << "\n";
    sort(idx.begin(), idx.end());
    for(int i=0; i<5; i++) cout << idx[i] << " ";
    return 0;
}
