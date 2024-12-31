def solution(numbers):
    stack = []  # 뒤에 큰 수가 있는지 확인하려는 index  (큰 수가 없다면 계속 남아있음)
    answer = [-1] * len(numbers)
    
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack[-1]] = num
            stack.pop()
            
        stack.append(i)
    return answer
