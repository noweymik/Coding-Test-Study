def solution(s):
    answer = ''
    
    if len(s) % 2 == 0: # 짝수글자라면        
        answer+= s[int(len(s)/2 -1)]
        answer+= s[int(len(s)/2)]
    else:
        answer+= s[len(s)//2]
    return answer