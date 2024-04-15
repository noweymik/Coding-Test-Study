def solution(s):
    process = 0 # 이진 변환 과정 개수
    zero_count = 0 # 변환과정에서 제거된 0의 총 개수
    
    # 1이 될 때까지 이진 변환
    while s != '1':        
        process += 1
        # 0의 개수 세기
        zero = s.count('0')
        # 0을 제거하여 다시 s 만들기
        s = '1' * (len(s)-zero)
        # s의 길이(c) 2진법으로 표현한 문자열을 s에 저장하기
        s = bin(len(s))[2:]
        zero_count += zero
    
    return [process, zero_count]