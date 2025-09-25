def solution(sizes):    
    max_size = 0
    for case in sizes:
        max_size = max([case[0], case[1], max_size])
    
    short = []
    for case in sizes:
        short.append(min(case[0], case[1]))
        
    answer = max_size * max(short)
    return answer