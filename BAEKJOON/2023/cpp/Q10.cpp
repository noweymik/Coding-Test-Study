// Baekjoon Q.1152
// 단어의 개수
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int count = 0;

    getline(cin, s);
    
    if(s.empty()) {
        cout << "0";
        return 0;
    }
    
    for(int i=0; i<s.length(); i++) {
        if(s[i]== ' ') {
            count++;
        }
    }

    //맨 앞 또는 맨 뒤 스페이스면 스페이스 개수 포함 x
    if(s[0] == ' ') count --;
    if(s[s.length()-1] == ' ') count--;

    cout << count + 1 << endl;
    return 0; 
}
