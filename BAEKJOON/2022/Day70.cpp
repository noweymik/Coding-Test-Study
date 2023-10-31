// Baekjoon Q.9295
// 주사위
#include <iostream>
using namespace std;

int main() {  
    int T;
    int t1, t2;
    
    cin >> T;
    for(int i=0; i<T; i++) {
        cin >> t1 >> t2;
        cout << "Case " << i+1 << ": " << t1+t2 << endl;
    }
    return 0;
}