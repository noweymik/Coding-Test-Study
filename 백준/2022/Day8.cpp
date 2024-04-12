// Baekjoon Q.25304
// 영수증
#include <iostream>
using namespace std;

int main() {
    int total = 0, cal_total = 0;
    int a, b, N = 0;

    cin >> total;
    cin >> N;

    for(int i=0; i<N; i++) {
        cin >> a >> b;
        cal_total += (a*b);
    }
    if(total == cal_total) cout << "Yes";
    else cout << "No";

    return 0;
}
