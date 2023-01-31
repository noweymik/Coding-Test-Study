// Baekjoon Q.2693
// N번째 큰 수
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, num;
    vector<int> v;
    cin >> n;
    for(int i=0; i<n; i++) {
        for(int k=0; k<10; k++) {
            cin >> num;
            v.push_back(num);
        }
        sort(v.begin(), v.end()); 
        cout << v[7] << endl;
        v.clear();
    }

   return 0; 
}
