# 백준 1316번  
# 그룹 단어 체커

N = int(input())
count = 0

for i in range(N):
    word = input()
    prev_w = []
    duplication = 0
    for idx in range(len(word)):
        if word[idx] not in prev_w:
            prev_w.append(word[idx])            
        elif word[idx] != prev_w[-1]:       # prev_w 리스트에 있지만 가장 마지막 알파벳과 다른 경우
            duplication = 1
            break
    if duplication == 0:
        count+=1    
    

print(count)
            