def solution(k, tangerine):
    answer = 0
    
    # 종류별 귤 개수 세기 (귤의 크기 : 귤의 개수)
    dict = {}
    for t in tangerine:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
    
    # 종류별 귤 개수 많은 순으로 sorting하기
    sorted_list = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    
    
    for num in sorted_list:
        size = num[0]
        if k <= 0:
            return answer
        else:
            k = k - dict[size]
            answer += 1
    
    return answer