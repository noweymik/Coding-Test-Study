// Baekjoon Q.11650
// 좌표 정렬하기
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {   
    int N, x, y;
    vector<pair<int,int>> coordinate;    

    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> x >> y;        
        coordinate.push_back({ x, y });  
    }

    sort(coordinate.begin(), coordinate.end());

    for(int i=0; i<N; i++) {
        cout << coordinate[i].first << ' ' << coordinate[i].second << "\n";
    }
    return 0;
}
