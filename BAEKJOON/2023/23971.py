# 백준 23971번
# ZOAC 4

import sys
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

seat = [[0,0]]
xlist = []
ylist = []

i = 1
while( i < W+1 ):
    if(i == 1):
        x = 1
    else:
        x = xlist[-1] + (M+1)
    i += (M+1)
    xlist.append(x)
    
j = 1
while( j < H+1 ):
    if(j == 1):
        y = 1
    else:
        y = ylist[-1] + (N+1)
    j += (N+1)
    ylist.append(y)

print(len(xlist) * len(ylist))