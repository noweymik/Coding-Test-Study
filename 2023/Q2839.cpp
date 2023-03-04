// Baekjoon Q.2839
// 설탕 배달
#include <iostream>

using namespace std;

int main() {
    int w = 0, five = 0, count = 0;
    cin >> w;

    while(w >= 0) { 
        if(w % 5 == 0) {
            five = w/5;
            count += five;
            cout << count << endl;
            return 0;
        }
        w -= 3; // 5로 나눠지지 않는다면 3키로 봉지 하나
        count++;
    }
    cout << -1 << endl;
    
    return 0;
}
