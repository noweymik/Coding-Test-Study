def solution(s):        
    stack = []
    
    for i in s:
        if len(stack) == 0:     # 빈 스택이면 값을 넣기
            stack.append(i)
        elif stack[-1] == i:    # 마지막 원소가 넣으려는 값과 일치하면 pop하기
            stack.pop()
        else:
            stack.append(i)     # 마지막 원소와 같지 않으면 값을 넣기
            
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
        
    return answer