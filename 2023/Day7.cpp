// Baekjoon Q.2752
// 세수정렬
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    vector<int> v;
    for(int i=0; i<3; i++) {
        cin >> n;
        v.push_back(n);
    }
    sort(v.begin(), v.end());
    for(int i=0; i<3; i++) cout << v[i] << " ";
    return 0;
}
