def solution(n, words):
    answer = []
        
    # 사람 번호를 알아낼 수 있는 것: (index % n) + 1    
    # 차례를 알아낼 수 있는 것: (index / n) + 1
    
    # 문제가 있으면 1, 없으면 0
    problem = 0 
    for i, w in enumerate(words):
        person_num = (i % n) + 1 
        order = int(i / n) + 1
        
        if i == 0:
            continue
            
        # 그 전 단어의 마지막 알파벳과 현재 단어의 첫번째 알파벳 비교
        if words[i-1][-1] != w[0]:            
            answer = [person_num, order]                
            problem = 1  
            break
            
        # 이전에 등장했었던 단어인지 확인
        if w in words[0:i-1]:
            answer = [person_num, order]
            problem = 1  
            break
        
    # 아무 문제가 없이 끝났다면
    if problem == 0:
        answer = [0,0]
    
    return answer