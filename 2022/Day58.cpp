// Baekjoon Q.10953
// A+B - 6
#include <iostream>
using namespace std;

int main() {     
    int N;
    int A, B;
    string input;
    cin >> N;

    for(int i=0; i<N; i++) {
        cin >> input;
        A = input[0] - '0';
        B = input[2] - '0';
        cout << A+B << endl;
    }
}

