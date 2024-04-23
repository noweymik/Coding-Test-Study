def solution(clothes):
    hash_map = {}
    
    for c in clothes:
        if c[1] not in hash_map:
            hash_map[c[1]] = [c[0]]            
        else:
            hash_map[c[1]].append(c[0])
        
    count = 1    
    # A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수 (N+1)(M+1)
    # -1 하는 이유는 모두 사용하지 않는 경우의 수 빼주기
    for h in hash_map:
        count *= (len(hash_map[h])+1)
        
    return count -1