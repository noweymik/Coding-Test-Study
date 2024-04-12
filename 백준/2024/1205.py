# 백준 1205번
# 등수 구하기

N, new, P = map(int, input().split())

if N == 0:
    output = 1
else:
    score_list = list(map(int, input().split()))
    
    rank_list = []
    for i in range(min(P, len(score_list))):
        rank_list.append(score_list[i])
        
    # 랭킹 리스트 마지막 점수보다 새로운 점수가 큰 경우 또는
    # 랭킹 리스트 개수보다 점수들 개수가 적은 경우
    if new > rank_list[-1] or N < P:        
        rank_list.append(new)
        rank_list.sort(reverse=True)
        output = rank_list.index(new) + 1        
    else:
        output = -1

print(output)


