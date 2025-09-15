import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []

for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)


dp = [0] * (N+1)
max_value = 0

for i in range(N-1, -1, -1):
    n_day = i + T[i]    # 현재 날짜 (i) + 상담 소요 기간 (T[i])
    if n_day <= N:      # 상담 가능
        dp[i] = max(P[i] + dp[n_day], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)