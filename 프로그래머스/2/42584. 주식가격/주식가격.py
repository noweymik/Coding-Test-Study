from collections import deque

def solution(prices):
    answer = []
    
    prices = deque(prices)
    while prices:        
        curr = prices.popleft()
        sec = 0        
        for p in prices:
            sec += 1
            # 주식 가격 떨어졌으면 break
            if curr > p:
                break                                            
        answer.append(sec)
    return answer