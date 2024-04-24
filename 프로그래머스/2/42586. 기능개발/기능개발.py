def solution(progresses, speeds):     
    days = [0] * len(progresses)
            
    # progresses 개수만큼 반복해서 각 progress마다 걸리는 작업일(days) 계산
    for i in range(len(progresses)):
        while True:
            if progresses[i] >= 100:
                break
            progresses[i] += speeds[i]
            days[i] += 1
                    
    answer = []
    
    while days:          
        top = days.pop(0)
        count = 1   # 배포될 수 있는 기능 개수
        
        # top과 days의 첫번째 원소를 비교 (top이 높으면 같이 배포 가능하니 pop)
        while days and top >= days[0]:             
            days.pop(0) 
            count += 1
        answer.append(count)                
    return answer