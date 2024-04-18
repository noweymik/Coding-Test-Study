def solution(n):
    # n의 2진수 1의 개수를 n_count에 넣기
    n_binary = format(n, 'b')
    n_count = 0
    
    for i in str(n_binary):
        if i == '1':
            n_count += 1
    
    # answer 첫 시작은 n + 1
    answer = n + 1    
    while True:
        binary = format(answer, 'b')
        count = 0
        for i in str(binary):
            if i == '1':
                count += 1
        # n의 1개수와 동일하면 멈추고 answer return하기
        if n_count == count:
            break
        # n의 1개수와 다르면 다음 큰 수로 넘어가기
        else:
            answer += 1
        
    return answer