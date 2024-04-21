def solution(participant, completion):
    answer = ''
    hash = {}
    
    # hash에 이름 넣기 -> 동명이인이면 value += 1
    for p in participant:
        if p in hash:
            hash[p] += 1
        else: 
            hash[p] = 1
    
    # 완주자가 hash에 있으면 value -= 1
    for c in completion:
        if c in hash:
            hash[c] -= 1

    # hash value가 1 이상인 사람 answer에 넣기
    for h in hash:
        if hash[h] >= 1:
            answer += h
    
    return answer