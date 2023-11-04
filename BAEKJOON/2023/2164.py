# 백준 2164번  
# 카드2
# 배운 점 : deque

from collections import deque

N = int(input())
card =deque()

for i in range(N):
    card.append(i+1)

while(len(card) > 1):
    card.popleft()
    card.append(card.popleft())
    
print(card[0])