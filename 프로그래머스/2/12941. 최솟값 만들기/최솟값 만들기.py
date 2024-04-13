def solution(A,B):
    answer = 0
    
    A.sort() 
    B.sort(reverse = True)
    
    # A의 최솟값과 B의 최댓값을 곱해서 넣는 방식
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer