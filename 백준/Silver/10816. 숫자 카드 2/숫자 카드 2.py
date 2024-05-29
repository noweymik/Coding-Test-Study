import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))
    
n_dict = {}
for n in N_list:
    if n in n_dict:
        n_dict[n] += 1
    else:
        n_dict[n] = 1        

N_list.sort()

# 이분 탐색
# 1. 자료를 오름차순으로 정렬
# 2. 자료의 중간값이 찾고자 하는 값인지 비교 (mid, target)    
# 3. mid와 target이 다르다면 대소 비교를 통해 탐색 범위 좁히고 target과 mid가 같아질 때까지 아래 조건에 따라 반복
    # step1. target이 mid값보다 작으면 end를 mid 왼쪽 값으로
    # step2. target이 mid값보다 크면 start를 mid 오른쪽 값으로

# --------- 1) 재귀 방법 -----------
def binary_search_recursive(target, list, start, end):
    # 못 찾을 경우    
    if start > end:
        return -1
                
    # 중간값 찾기            
    mid = (start + end) // 2
    
    # mid값과 같으면 return
    if list[mid] == target:
        return n_dict.get(target)
    # mid값보다 작으면 end 값 변경해서 재귀
    elif list[mid] > target:
        end = mid - 1
    # mid값보다 크면 start 값 변경해서 재귀
    elif list[mid] < target:
        start = mid + 1   

    return binary_search_recursive(target, list, start, end)

for m in M_list:      
    if binary_search_recursive(m, N_list, 0, len(N_list)-1) == -1: # 못 찾은 경우  
        print(0, end=' ')
    else: 
        print(binary_search_recursive(m, N_list, 0, len(N_list)-1), end=' ')
# --------- 1) 재귀 방법 -----------

        
        
# --------- 2) 반복문 방법 -----------
# def binary_search_iter(target, list):
#     start = 0
#     end = len(list) - 1
    
#     while start <= end:
#         mid = (start + end) // 2
#         if list[mid] == target:
#             # target이 있으면 n_dict의 value값을 찾아서 return하기
#             return n_dict.get(target)
#         elif list[mid] > target:
#             end = mid - 1
#         elif list[mid] < target:
#             start = mid + 1    
    
#     # target을 list에서 못 찾은 경우 
#     return -1
    
# for m in M_list:      
#     if binary_search_iter(m, N_list) == -1: # 못 찾은 경우  
#         print(0, end=' ')
#     else: 
#         print(binary_search_iter(m, N_list), end=' ')
# --------- 2) 반복문 방법 -----------
