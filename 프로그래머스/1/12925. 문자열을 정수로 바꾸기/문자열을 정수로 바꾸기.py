def solution(s):
    if s[0] == '-':
        answer = int(s[1:]) * -1
    elif s[0] == '+':
        answer = int(s[1:]) 
    else:  # 양수인데 + 안 붙은 경우
        answer = int(s) 
    return answer