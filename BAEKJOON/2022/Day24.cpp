// Baekjoon Q.15596
// 정수 N개의 합
#include <vector>

long long sum(std::vector<int> &a) {
	long long ans = 0;
    for(auto x : a) {
        ans += x;
    }
	return ans;
}
