import math

def solution(progresses, speeds): 
    answer = []
    days = []    
    for i, p in enumerate(progresses):                
        days.append(math.ceil((100 - p) / speeds[i]))    
    
    top = days.pop(0)
    count = 1
    while days:        
        if top >= days[0] and days:
            days.pop(0)
            count += 1
        else:
            answer.append(count)
            count = 0
            if days:            
                top = days.pop(0)
                count = 1
    answer.append(count)
    return answer