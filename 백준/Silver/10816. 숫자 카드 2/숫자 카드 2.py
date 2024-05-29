import sys
input = sys.stdin.readline

N = int(input())
N_list = sorted(list(map(int, input().split())))

M = int(input())
M_list = list(map(int, input().split()))
    
n_dict = {}
for n in N_list:
    if n in n_dict:
        n_dict[n] += 1
    else:
        n_dict[n] = 1        
        
def binary_search_iter(target, list):
    start = 0
    end = len(list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            # target이 있으면 n_dict의 value값을 찾아서 return하기
            return n_dict.get(target)
        elif list[mid] > target:
            end = mid - 1
        elif list[mid] < target:
            start = mid + 1    
    
    # target을 list에서 못 찾은 경우 
    return -1
    
for m in M_list:      
    if binary_search_iter(m, N_list) == -1: # 못 찾은 경우  
        print(0, end=' ')
    else: 
        print(binary_search_iter(m, N_list), end=' ')
