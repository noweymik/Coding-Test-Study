def solution(answers):
    answer = [] 
    # 점수를 담을 dict
    count = {1 : 0, 2 : 0, 3 : 0}
    # 1번 : 12345
    # 2번 : 21232425
    # 3번 : 3311224455
    person_1 = [1,2,3,4,5]
    person_2 = [2,1,2,3,2,4,2,5]
    person_3 = [3,3,1,1,2,2,4,4,5,5]
    
    
    for index, a in enumerate(answers):
        if a == person_1[index % 5]:
            count[1] += 1
        if a == person_2[index % 8]:
            count[2] += 1
        if a == person_3[index % 10]:
            count[3] += 1
    
    # 가장 높은 점수
    max_value = max(count.values())
    # 가장 높은 점수를 가진 모든 사람을 answer list에 넣기
    for c in count:        
        if count[c] == max_value:
            answer.append(c)

    return answer