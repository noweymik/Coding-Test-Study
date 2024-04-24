def solution(arr):    
    # first in last out
    stack = []    
    for a in arr:
        # stack이 empty하지 않고 마지막 원소가 a가 아닌 경우
        if stack and stack[-1] == a:
                continue
        # stack이 empty한 경우거나 마지막 원소가 a가 아닌 경우
        else:
            stack.append(a)    
    return stack