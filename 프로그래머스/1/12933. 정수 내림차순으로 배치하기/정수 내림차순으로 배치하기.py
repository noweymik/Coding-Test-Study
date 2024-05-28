def solution(n):    
    answer_str = ""    
    str_n = str(n)
    number = []
    
    for i in range(len(str_n)):
        number.append(int(str_n[i]))
    
    number.sort(reverse=True)
    
    for num in number:
        answer_str += str(num)
        
    return int(answer_str)