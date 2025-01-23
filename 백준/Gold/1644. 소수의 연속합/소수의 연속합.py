import sys
import math
input = sys.stdin.readline

N = int(input())

prime_check = [False, False] + [True] * (N-1)   # N+1개의 list (0부터 N까지)
prime_num_list = [] # N보다 낮은 소수 list

# 에라토스테네스의 체 알고리즘
# 소수의 배수는 소수가 아니라는 사실을 이용해 배수를 제거하는 것
for i in range(2, int(math.sqrt(N))+1):    
    if prime_check[i]:
        for j in range(i*i, N+1, i):
            prime_check[j] = False


for i in range(len(prime_check)):
    if prime_check[i]:
        prime_num_list.append(i)


if not prime_num_list:  # 소수가 없는 경우 예외 처리
    print(0)
    sys.exit()

sub_sum = prime_num_list[0]
i, j = 0, 0
count = 0

while(True):
    if sub_sum == N:
        count += 1
        sub_sum -= prime_num_list[i]
        i += 1
        
    elif sub_sum < N:
        j += 1
        if j == len(prime_num_list):
            break
        sub_sum += prime_num_list[j]
                
    elif sub_sum > N:
        sub_sum -= prime_num_list[i]
        i += 1

print(count)