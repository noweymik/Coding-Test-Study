// Baekjoon Q.2438
// 별찍기 -1
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    for(int i=1; i<=N; i++) {
        for(int j=1; j<=i; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
