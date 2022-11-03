// Baekjoon Q.11720
// 숫자의 합
#include <iostream>
using namespace std;

int main() { 
    int N, sum = 0;   
    string s;
    cin >> N;
    cin >> s;

    for(int i=0; i<N; i++) {
        sum += s[i]-'0';
    }
    cout << sum;
    return 0;
}