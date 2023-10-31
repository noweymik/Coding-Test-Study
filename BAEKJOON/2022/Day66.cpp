// Baekjoon Q.10886
// 0 = not cute / 1 = cute
#include <iostream>
using namespace std;

int main() {  
    int N, vote;
    int not_cute = 0, cute = 0;
    cin >> N;

    for(int i=0; i<N; i++) {
        cin >> vote;
        if(vote == 0) not_cute++;
        else if(vote ==1) cute++;
    }
    
    if(not_cute > cute) cout << "Junhee is not cute!";
    else cout << "Junhee is cute!";
}