// Baekjoon Q.2562
// 최댓값
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, max = 0, max_index;
    vector<int> v;

    for(int i=0; i<9; i++) {
        cin >> n;
        v.push_back(n);
    }
    for(int k=0; k<v.size(); k++) {
        if(v[k] > max) {
            max = v[k];
            max_index = k+1;
        }
    }
    cout << max << endl;
    cout << max_index;        
    return 0;
}