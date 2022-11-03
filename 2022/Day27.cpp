// Baekjoon Q.10809
// 알파벳 찾기 
#include <iostream>
using namespace std;

int main() { 
    string s;
    int alphabet[26];
    for(int i=0; i<26; i++) alphabet[i] = -1;

    cin >> s;

    for(int i=0; i<s.length(); i++) {
        if(alphabet[s[i]-'a']==-1) alphabet[s[i]-'a'] = i;
    }
    for(int i=0; i<26; i++) {
        cout << alphabet[i] << " ";
    }
    return 0;
}