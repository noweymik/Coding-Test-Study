def solution(n):
    answer = 0
        
    i = 0
    a, b = 0, 1
    
    while(i < n-1):
        c = a + b        
        if i == n-2:
            answer = c
            break
        a = b
        b = c        
        i += 1
    answer = answer % 1234567
    return answer