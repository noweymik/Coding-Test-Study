// Baekjoon Q.2480
// 주사위 세개
#include <iostream>
using namespace std;

int main() {     
    int dice[3]; // results of dice
    int money = 0, max = 0;
    
    for(int i=0; i<3; i++) cin >> dice[i];

    if(dice[0] == dice[1] && dice[1] == dice[2]) {
        money = 10000 + dice[0] * 1000;
    }
    else if(dice[0] == dice[1]) {
        money = 1000 + dice[0] *100;
    }
    else if(dice[1] == dice[2]) {
        money = 1000 + dice[1] *100;
    }
    else if(dice[0] == dice[2]) {
        money = 1000 + dice[0] *100;
    }
    else {
        for(int i=0; i<3; i++) {
            if(max < dice[i]) max = dice[i];
        }
        money = max * 100;
    }

    cout << money;
    return 0;
}
