# 백준 11047번  
# 동전 0
# 배운 점 : 나눗셈 /와 //의 차이 (/의 결과 : float, //의 결과 : int)

N, K = map(int, input().split())
coin = []

for i in range(N):
    coin.append(int(input()))

count = 0

while(K > 0):
    max_coin = 0
    for c in coin:
        if(c > max_coin and c <= K):
            max_coin = c
    
    count += K // max_coin
    K = K % max_coin

    if (K==0):
        break

print(count)