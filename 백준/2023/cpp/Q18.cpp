// Baekjoon Q.1920
// 수 찾기
#include <iostream>
#include <algorithm>
using namespace std;

int a[100010];

int BinarySearch(int key, int size) {
    int start = 0;
    int end = size-1;
    int mid;

    while(start <= end) {
        mid = (start + end) / 2;
        
        if(a[mid] == key) 
            return 1;
        else if(a[mid] > key)
            end = mid - 1;
        else if(a[mid] < key)
            start = mid + 1;
    }
    return 0;
}
int main() {
    int N, M;
    int num;
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> num;
        a[i] = num;
    }
    sort(a, a+N); // quick sort

    cin >> M;
    for(int i=0; i<M; i++) {
        cin >> num;
        printf("%d\n", BinarySearch(num, N));
    }

    return 0;
}
