# 백준 2607번
# 비슷한 단어

import sys
input = sys.stdin.readline

N = int(input())

word = list(input())
count = 0

for i in range(1, N):
    firstword = word[:]
    checkword = input()
    diff = 0

    for w in checkword:
        if w in firstword:
            firstword.remove(w)
        else:
            diff += 1
    if  diff <= 1 and len(firstword) <= 1:
        count+=1
        
print(count)