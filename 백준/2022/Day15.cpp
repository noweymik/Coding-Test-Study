// Baekjoon Q.5597
// 과제 안 내신 분..?
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int array[30] = {0};
    vector<int> student;
    int num;
    for(int i=0; i<28; i++) {
        cin >> num;
        array[num-1]++;
    }
    for(int j=0; j<30; j++) {
        if(array[j]==0) student.push_back(j+1);        
    }

    sort(student.begin(), student.end());
    for(auto x : student) {
        cout << x << endl;
    }

    return 0;
}
