def solution(nums):
    answer = 0
    Ponkemon = {}
    
    for n in nums:
        if n not in Ponkemon:
            Ponkemon[n] = 1
        else:
            Ponkemon[n] += 1
    
    if len(nums)/2 <= len(Ponkemon): # N/2마리 폰켓몬 개수만큼 종류가 있다면 N/2 return
        answer = len(nums)/2    
    else:       # N/2마리 폰켓몬 개수보다 종류가 적다면 종류 개수 return
        answer = len(Ponkemon)
    return answer