def solution(x, y, n):
    # 1e9 : 1∗10^9 = 1,000,000,000 
    
    DP = [1e9 for _ in range(y + 1)]
    DP[x] = 0
    
    for i in range(x, y + 1):
        # n을 더하는 경우
        if i + n <= y:
            DP[i + n] = min(DP[i + n], DP[i] + 1)
        # 2을 곱하는 경우
        if i * 2 <= y:
            DP[i * 2] = min(DP[i * 2], DP[i] + 1)
        # 3을 곱하는 경우
        if i * 3 <= y:
            DP[i * 3] = min(DP[i * 3], DP[i] + 1)
    
    # 최솟값이 만들어지지 않는 경우
    if DP[y] == 1e9:
        return -1
    
    return DP[y]