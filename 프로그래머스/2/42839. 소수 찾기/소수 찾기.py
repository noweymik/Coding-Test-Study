from itertools import permutations

def check_prime(num):
    if num < 2:
        return False
    if num == 2:
        True
        
    for i in range(2, num):
        if num % i ==0:
            return False        
    return True


def solution(numbers):
    num_list = list(numbers)

    check_list = set()
    for i in range(1, len(num_list)+1):   
        per_list = permutations(num_list, i)
        
        for p in per_list:
            check_list.add(int(''.join(p)))    
    
    answer = 0
    for n in check_list:
        if check_prime(n):
            answer += 1        
        
    return answer