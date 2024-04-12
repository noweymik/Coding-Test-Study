# 백준 25757번  
# 임스와 함께하는 미니게임

import sys
input = sys.stdin.readline

N, game = input().split()
N = int(N)
users = []

for i in range(N):
    users.append(input())
    
temp = set(users)
user_list = list(temp)

if game == 'Y':
    print(len(user_list))
elif game == 'F':
    print(int(len(user_list) / 2))
elif game == 'O':
    print(int(len(user_list) / 3))