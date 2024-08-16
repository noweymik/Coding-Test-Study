def solution(s):
    answer = ''
    word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    word = ''
    for i in s:
        if i.isdigit(): # 숫자면 answer에 추가하고 다음 반복문으로
            answer += i
            continue
        word += i                                   # 숫자가 아니면 word에 추가
        if word in word_list:                       # 만들어진 word가 word_list에 있다면
            answer += str(word_list.index(word))    # answer에 추가
            word = ''                               # word 초기화
    
    answer = int(answer) 
    return answer
