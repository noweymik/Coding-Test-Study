# 백준 15649번  
# N과 M (1)
# 배운 점 : itertools

from itertools import *

N, M = map(int, input().split())
dataset = []
for i in range(N):
    dataset.append(i+1)
    
printList = list(permutations(dataset, M))
for p in printList:
    for m in range(M):
        print(p[m], end=" ")
    print()