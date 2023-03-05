// Baekjoon Q.1181
// 단어 정렬
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(string a, string b) {
    if (a.length() == b.length()) {
        return a < b;
    }
    return a.length() < b.length();
}

int main() {
    int N;
    vector<string> s;

    cin >> N;
    
    for(int i=0; i<N; i++) {
        string word;
        cin >> word;

        //중복 검사
        if(find(s.begin(), s.end(), word) == s.end()) {
            s.push_back(word);
        }        
    }

    sort(s.begin(), s.end(), compare);

    for(int i=0; i<s.size(); i++) {
        cout << s[i] << "\n";
    }
    return 0;
}
