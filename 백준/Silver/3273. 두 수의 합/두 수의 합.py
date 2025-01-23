import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
X = int(input())

num_list.sort()

count = 0
i = 0
j = N - 1

while(i < j):
    sum = num_list[i] + num_list[j]
    if sum == X:
        count += 1
        i += 1
    elif sum < X:
        i += 1
    elif sum > X:
        j -= 1

print(count)
    