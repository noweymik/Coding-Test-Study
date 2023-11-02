# 백준 7568번  
# 덩치

N = int(input())
data = []
rank = []
for i in range(N):
    x, y = map(int, input().split())
    data.append((x,y))
    
for i in range(N):
    r = 0
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            r += 1
    rank.append(r+1)
    
for k in rank:
    print(k, end=" ")
    




            
            
        
    
    
    