// Baekjoon Q.2587
// 대표값2
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {     
    vector<int> num;
    int input, sum = 0;
    
    for(int i=0; i<5; i++) {
        cin >> input;
        num.push_back(input);
        sum += num[i];
    }
    sort(num.begin(), num.end());
    cout << sum/5 << endl;
    cout << num[2] << endl;

    return 0;
}
