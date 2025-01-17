n, k = map(int, input().split())
temp = list(map(int, input().split()))


sum_list = [sum(temp[:k])]

for i in range(n-k):
    sum_list.append(sum_list[i] - temp[i] + temp[i+k])
    
print(max(sum_list))