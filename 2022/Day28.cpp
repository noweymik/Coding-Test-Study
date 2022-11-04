// Baekjoon Q.2675
// 문자열 반복
#include <iostream>
using namespace std;

int main() { 
    int T, R;           // T: 케이스의 개수, R: 반복 횟수
    string s, new_s;  

    cin >> T;
    for(int i=0; i<T; i++) {
        cin >> R;
        cin >> s;
        for(int k=0; k<s.length(); k++) {
            for(int n=0; n<R; n++) new_s += s[k];            
        }
        cout << new_s << endl;
        new_s = ""; 
    }    
    return 0;
}