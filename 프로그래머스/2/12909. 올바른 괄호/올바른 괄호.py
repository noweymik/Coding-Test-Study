def solution(s):
    
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:               # i가 ")" 일 때,
            if not stack:   # empty한 상태라면
                return False
            else:           # stack에 있는 짝 "(" 을 제거하기
                stack.pop()
            
    # stack이 empty한 상태라면 모두 바르게 짝지어졌다는 뜻            
    return len(stack) == 0