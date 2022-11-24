// Baekjoon Q.11650
// 좌표 정렬하기
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {   
    int N, num;
    vector<int> v;    

    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> num;
        v.push_back(num);  
    }

    sort(v.begin(), v.end());

    for(int i=0; i<N; i++) {
        cout << v[i] << "\n";
    }
    return 0;
}
