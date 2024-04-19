def solution(arr):
    a = max(arr)    # arr 요소 중 가장 큰 수
    b = 1           # arr 모든 요소를 곱한 수 
    for i in arr:
        b *= i 
    
    
    # arr 중 가장 큰 수부터, arr 모든 요소를 곱한 수까지
    for num in range(a, b + 1):
        check = True
        # 만약 arr의 각 요소로 나누었을 때 모두 나머지가 0인 경우 => 최소 공배수 찾음!
        for k in arr:
            if num % k == 0:
                check = True
            else:   # 하나라도 나머지가 0이 아닌 경우 -> 최소 공배수 아님
                check = False
                break
        # 각 요소 모두 나머지가 0인 경우
        if check is True:      
            answer = num
            break
    return answer