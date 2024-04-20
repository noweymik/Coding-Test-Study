def solution(n):
    answer = 0
    number = []
    for i in range(1, n+1):
        if n % i == 0:
            number.append(i)
    answer = sum(number)
    return answer