import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))


count = 0
i = 0
j = 0

while(i < N and j <= N):
    total = sum(A[i:j+1])        
    if total == M:
        count += 1
        if i <= j:
            i += 1
            j = i
    elif total < M:
        j += 1
    elif total > M:
        i += 1
        
print(count)