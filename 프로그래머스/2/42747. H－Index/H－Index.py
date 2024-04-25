def solution(citations):    
    citations.sort()    
    for i, c in enumerate(citations):
        if c >= (len(citations) - i):    
            return len(citations) - i
    return 0
    