import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    
    total = 0  
    max_price = 0
    
    # 역방향으로 검사
    for i in range(N-1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:   # 현재 주가가 미래 주가보다 낮을 경우 (미래 max 주가에 팔기)
            total += max_price - price[i]

    print(total)