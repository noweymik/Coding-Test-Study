// Backjoon Q.2083
// 럭비 클럽
#include <iostream>

using namespace std;

int main() {
    string name;
    int age;
    int weight;
    while (true) {
        cin >> name >> age >> weight;
        if(name == "#" && age == 0 && weight ==0) break;
        if(age > 17 || weight >= 80) {
            cout << name << " Senior" << endl;
        }
        else {
            cout << name << " Junior" << endl;
        }   
    }
    return 0;
}