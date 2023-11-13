# 백준 11053번  
# 가장 긴 증가하는 부분 수열
# 배운 점 : LIS 알고리즘

N = int(input())
seq = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if(seq[i] > seq[j]):
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# 틀린 풀이법 ㅠㅠ
# N = int(input())
# seq = list(map(int, input().split()))
# seq_after = [1] * N

# for index, a in enumerate(seq):
#     min = a
#     for i in range(index, N):
#         if(min < seq[i]):
#             min = seq[i]
#             seq_after[index] += 1

# print(max(seq_after))