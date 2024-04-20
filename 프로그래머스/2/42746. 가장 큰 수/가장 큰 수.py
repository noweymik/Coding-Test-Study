def solution(numbers):
    answer = ''

    # numbers list를 string 형태로 변환해서 temp에 담기
    temp = list(map(str, numbers))
    # 문자열 3번 반복해서 정렬 (ex 3, 30 비교시 -> 333 303030 비교 -> 333 우선)
    temp.sort(key = lambda x : x * 3, reverse = True)
    for n in temp:        
        answer += str(n)
    # 0000인 경우 -> 0으로 바꾼 후 다시 string 변환해줘야함
    answer = str(int(answer))
    return answer