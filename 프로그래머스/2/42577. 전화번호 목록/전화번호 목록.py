def solution(phone_book):
    answer = True
        
    hash_map = {}    
    for n in phone_book:
        hash_map[n] = 1
    
    for numbers in hash_map:
        prefix = ""
        for num in numbers:            
            prefix += num
            # 자기 자신이 아니고, 접두어가 hash_map에 있으면!
            if prefix in hash_map and prefix != numbers:
                answer = False
            
    return answer