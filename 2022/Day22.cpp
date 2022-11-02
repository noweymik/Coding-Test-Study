// Baekjoon Q.2566
// 최댓값
#include <iostream>
using namespace std;

int main() {
    int num, max = 0, max_row, max_col;

    for(int i=0; i<9; i++) {
        for(int j=0; j<9; j++) {
            cin >> num;
            if(num >= max) {
                max = num;
                max_row = i+1;
                max_col = j+1;
            }
        }
    }
    cout << max << endl;
    cout << max_row << " " << max_col;
    return 0;
}