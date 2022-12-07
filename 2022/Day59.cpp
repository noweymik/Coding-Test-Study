// Baekjoon Q.2751
// 수 정렬하기 2
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {     
    int N, num; // N: 숫자 개수
    vector<int> v;
    
    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> num;
        v.push_back(num);
    }   
    sort(v.begin(), v.end());   // 오름차순 정렬
    for(int i=0; i<N; i++) {
        cout << v[i] << '\n';
    }
}

