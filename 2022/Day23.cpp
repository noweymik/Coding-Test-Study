// Baekjoon Q.2563
// 색종이
#include <iostream>
using namespace std;

int main() {    
    int N;          // 색종이 개수 
    int p[100][100] = {0};
    int a,b;        // a: 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리, b: 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리
    int sum = 0;    // 색종이가 붙은 검은 영역의 넓이
    cin >> N;

    for(int k=0; k<N; k++) {
        cin >> a >> b;
        for(int i=0; i<10; i++){
            for(int j=0; j<10; j++) {
                p[a+i][b+j] = 1;
            }
        }
    }
    for(int i=0; i<100; i++) {
        for(int j=0; j<100; j++) {
            if(p[i][j]==1) sum++;
        }
    }
    cout << sum;

    return 0;
}