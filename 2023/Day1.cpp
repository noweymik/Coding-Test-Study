// Baekjoon Q.10178 
// 할로윈의 사탕
#include <iostream>

using namespace std;

int main() {
    int n;
    int c, v;

    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> c >> v;
        cout << "You get " << c/v << " piece(s) and your dad gets " << c%v << " piece(s)." << endl; 
    }

    return 0;
}
