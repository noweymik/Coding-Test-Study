// Baekjoon Q.10814
// 나이순 정렬
#include <iostream>
#include <map>

using namespace std;

int main() {
    int N;
    int age;
    string name;
    multimap<int, string> m; // multimap은 중복 키 허용
    
    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> age >> name;
        m.insert(make_pair(age, name));
    }

    for (auto x : m) {
        cout << x.first << " " << x.second << "\n";
    }
    return 0;
}
