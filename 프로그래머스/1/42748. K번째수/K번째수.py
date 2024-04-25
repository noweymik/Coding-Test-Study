def solution(array, commands):
    answer = []
    
    for c in commands:        
        temp = []
        # i부터 j까지 원소들 temp에 넣기
        for idx in range(c[0]-1, c[1]):
            temp.append(array[idx]) 
        # temp 정렬
        temp.sort()        
        answer.append(temp[c[2]-1])           
    return answer

