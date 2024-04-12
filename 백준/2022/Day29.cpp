// Baekjoon Q.2908
// 상수
#include <iostream>
#include <string> 
using namespace std;

int main() { 
    int A, B;
    string s_A, s_B;
    cin >> A >> B;
        
    s_A += to_string((A%100)%10);   // 일의 자리수 
    s_A += to_string((A%100)/10);   // 십의 자리수 
    s_A += to_string(A/100);        // 백의 자리수

    s_B += to_string((B%100)%10);
    s_B += to_string((B%100)/10);    
    s_B += to_string(B/100);

    if(stoi(s_A) < stoi(s_B)) cout << s_B << endl;
    else cout << s_A << endl;
    return 0;
}
