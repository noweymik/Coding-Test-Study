def solution(n):
    answer = []
    str_n = str(n)
    
    for i in range(len(str_n)-1, -1, -1):
        answer.append(int(str_n[i]))
    
    return answer