height = []

for i in range(9):
    height.append(int(input()))

height.sort()

total = sum(height)
i = 0
j = len(height) - 1


while(i != j):
    sum = total - height[i] - height[j]
        
    if sum == 100:
        for k in range(9):
            if k != i and k != j:
                print(height[k])
        break   
    
    elif sum > 100:
        i += 1
        
    elif sum < 100:
        j -= 1