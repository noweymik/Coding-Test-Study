# 백준 2798번  
# 블랙잭

from itertools import *

N, M = map(int, input().split())

card = list(map(int, input().split()))

select_three_cards = list(combinations(card, 3))

best = 0
for i in select_three_cards:
    if(sum(i) > best and sum(i) <= M):
        best = sum(i)

print(best)
    