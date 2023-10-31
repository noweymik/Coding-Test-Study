// Baekjoon Q.2738
// 행렬 덧셈
#include <iostream>

using namespace std;

int main() {
    int N, M, num;
    cin >> N >> M;
    
    int** A = new int*[N];  // 2차원 배열 동적 할당 (row size)
    int** B = new int*[N];
    
    for(int i=0; i<N; i++) {    // col size
        A[i] = new int[M];
        B[i] = new int[M];
    }
    // A
    for(int i=0; i<N; i++) {        // row
        for(int j=0; j<M; j++) {    // col
            cin >> num;            
            A[i][j] = num;
        }       
    }
    // B
    for(int i=0; i<N; i++) {        // row
        for(int j=0; j<M; j++) {    // col
            cin >> num;
            B[i][j] = num;
        }       
    }
    // Answer (A+B)
    for(int i=0; i<N; i++) {        // row
        for(int j=0; j<M; j++) {    // col
            cout << A[i][j] + B[i][j] << " ";
        }  
        cout << endl;
    }
    
    // 할당 해제
    for(int i=0; i<N; i++) {    
        delete[] A[i];
        delete[] B[i];
    }
    delete[] A;
    delete[] B;
    
    return 0;
}
