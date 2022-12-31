// Baekjoon Q.1550
// 16진수 -> 고치기
#include <iostream>
#include <cmath>
using namespace std;

int main() {  
    string input; // Hexadecimal
    int num;
    int decimal = 0;

    cin >> input;

    for(int i=1; i<=input.length(); i++) {
        
        if(input[i] == 'A') {
            decimal += 10 * pow(16, input.length()-i);
        }
        else if(input[i] == 'B'){
            decimal += 11 * pow(16, input.length()-i);
        }
        else if(input[i] == 'C'){
            decimal += 12 * pow(16, input.length()-i);
        }
        else if(input[i] == 'D'){
            decimal += 13 * pow(16, input.length()-i);
        }
        else if(input[i] == 'E'){
            decimal += 14 * pow(16, input.length()-i);
        }
        else if(input[i] == 'F'){
            decimal += 15 * pow(16, input.length()-i);
        }
        else {
            decimal += input[i] * pow(16, input.length()-i);
        }
    }

    cout << decimal;
}