// Baekjoon Q.2588
// 곱셈
#include <iostream>
using namespace std;

int main() {     
    int num1, num2;
    cin >> num1;
    cin >> num2;    
    
    int num2_1 = num2 % 10;                         // num2의 일의 자리수
    int num2_10 = (num2 - (num2/100)*100) / 10;     // num2의 십의 자리수
    int num2_100 = num2 / 100;                      // num2의 백의 자리수
    
    cout << num2_1 * num1 << endl;
    cout << num2_10 * num1 << endl;
    cout << num2_100 * num1 << endl;
    cout << num1 * num2 << endl;
    return 0;
}

