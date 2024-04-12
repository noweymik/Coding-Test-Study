# 백준 20125번  
# 쿠키의 신체 측정

N = int(input())
list = [['_' for x in range(N)] for y in range(N)]

for i in range(N):
    list[i] = input().strip()
    
heart_r, heart_c = 0, 0

for i in range(N):
    for j in range(N):
        if list[i][j] == '*':
            heart_r = i+1
            heart_c = j
    if heart_r != 0:
        break
    
left_arm ,right_arm = 0, 0

for j in range(N):
    if j < heart_c:         
        if list[heart_r][j] == '*':
            left_arm += 1
    elif j > heart_c:
        if list[heart_r][j] == '*':
            right_arm += 1

waist = 0

for i in range(heart_r+1, N):
    if list[i][heart_c] == '*':
        waist += 1

left_leg, right_leg = 0, 0

for i in range(heart_r+1, N):
    if list[i][heart_c-1] == '*':
        left_leg += 1
    if list[i][heart_c+1] == '*':
        right_leg += 1
                
print("{} {}".format(heart_r+1, heart_c+1))
print("{} {} {} {} {}".format(left_arm, right_arm, waist, left_leg, right_leg))
