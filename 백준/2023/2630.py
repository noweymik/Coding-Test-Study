# 백준 2630번  
# 색종이 만들기

import sys
input = sys.stdin.readline

N = int(input())

matrix = [[] for _ in range(N)]
for i in range(N):
    matrix[i] = input().split(" ")

blue = 0
white = 0

def func(x, y, N):
    global b, w
    