// Baekjoon Q.8958
// OX 퀴즈
#include <iostream>
using namespace std;

int main() {
    int N, bonus, total;
    string line;       
    cin >> N;

    for(int i=0; i<N; i++) {
        cin >> line;
        bonus = 0, total =0;
        for(auto x : line) {            
            if(x == 'O') {
                bonus ++;
                total += bonus;
            }
            else { // x == 'X'
                bonus = 0;
            }
        }
        cout << total << endl;
    }

    return 0;
}