// Baekjoon Q.10818
// 최소, 최대
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    int min = 1000000, max = -1000000;
    cin >> N;
    
    vector<int> v; 
    int num;   
    for(int i=0; i<N; i++) {
        cin >> num;
        v.push_back(num);
    }
    for(auto x : v) {
        if(x >= max) max = x;
        if(x <= min) min = x;
    }
    cout << min << " " << max;
    return 0;
}
