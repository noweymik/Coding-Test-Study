def solution(s):
    answer = []
    word = s.split(" ")
    
    for w in word:        
        if w:            
            answer.append(w[0].upper() + w[1:].lower())
        else:
            answer.append(w)
            
    return " ".join(answer)