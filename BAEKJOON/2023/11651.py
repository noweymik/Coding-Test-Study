# 백준 11651번  
# 좌표 정렬하기 2

N = int(input())
list= []

for i in range(N):
    num_x, num_y = map(int, input().split(" "))
    list.append((num_x,num_y))

list.sort(key = lambda k: (k[1], k[0]))

for x, y in list:
    print(x, end=" ")
    print(y)