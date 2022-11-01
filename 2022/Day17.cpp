// Baekjoon Q.10807
// 개수 세기
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, v, num, count = 0;
    cin >> N;

    vector<int> vector;
    for(int i=0; i<N; i++) {
        cin >> num;         
        vector.push_back(num);
    }
    cin >> v;
    for(auto x : vector) {
        if(x == v) count ++;
    }
    cout << count;
    return 0;
}