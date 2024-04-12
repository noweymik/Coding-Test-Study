# 백준 2512번  
# 예산

from sys import stdin
input = stdin.readline

N = int(input())
budget = list(map(int, input().split()))
total = int(input())

start, end = 0, max(budget)

while start <= end:
    mid = (start+end) // 2 # 몫
    sum = 0
    for b in budget:
        sum += min(b, mid)
                
    if sum <= total: # 한도를 넘지 않는 경우
        start = mid + 1
    else:
        end = mid - 1

print(end)
