from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))
    
    while(people):        
        if len(people) >= 2:
            w = people[0] + people[-1] 
            if w <= limit:                
                people.popleft()    # 최댓값 빼내기    
                people.pop()        # 최솟값 빼내기
            else:
                people.popleft()
        else:
            people.popleft()            
        answer += 1        
        
    return answer