// Baekjoon Q.10871
// X보다 작은 수
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, X, num;
    cin >> N >> X;

    vector<int> ans;
    for(int i=0; i<N; i++) {
        cin >> num;         
        if(num < X) ans.push_back(num);
    }
    for(auto x : ans) {
        cout << x << " ";
    }
    return 0;
}