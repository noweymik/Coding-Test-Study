import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

i, j = 0, 0
length = 100001
sub_sum = num_list[0]

while(True):        
    if sub_sum >= S:        
        length = min(length, j + 1 - i)            
        sub_sum -= num_list[i]
        i += 1              
        
    elif sub_sum < S:        
        j += 1
        if j < N:            
            sub_sum += num_list[j]            
        else:
            break

if length == 100001:    
    print(0)
else:
    print(length)