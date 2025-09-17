import sys
import math
input = sys.stdin.readline

# 응시장별로
# 응시자 수 : A
# 총감독관 수 : 1
# 부감독관이 봐야할 응시자 수 : remain = A - B
# 부감독관이 봐야할 응시자 수가 1명 이상이면
    # 부감독관 수 :  ( A - B ) / C 

N = int(input())

A_list = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for a in A_list:
    result += 1
    remain = a - B
    if remain > 0:
        result += math.ceil(remain/C)
    
print(result)