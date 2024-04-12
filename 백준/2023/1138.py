# 백준 1138번
# 한 줄로 서기
# 배운 점 : * Operator to Print a Python List

import sys
input = sys.stdin.readline

N = int(input())

info = list(map(int, input().split()))
height = [0] * N

for i in range(N):
    count = 0
    for j in range(N):
        if count == info[i] and height[j] == 0:
            height[j] = i + 1
            break
        elif height[j] == 0:
            count += 1
            
print(*height)