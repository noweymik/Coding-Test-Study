// Baekjoon Q.11021
// A+B-7
#include <iostream>
using namespace std;

int main() {
    int A, B;
    int T;
    
    cin >> T;
    for(int i=1; i<=T; i++) {
        cin >> A >> B;
        cout << "Case #" << i << ": " << A+B << endl;
    }
    return 0;
}