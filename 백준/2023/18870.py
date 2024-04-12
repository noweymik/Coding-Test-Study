# 백준 18870번  
# 좌표 압축
# 배운 점 : 중복 제거 - set 이용, index와 같이 반복 - enumerate 

N = int(input())

X = list(map(int, input().split()))
X_set = sorted(set(X))

dict = {num : index for index, num in enumerate(X_set)}

for i in X:
    print(dict[i], end = " ")
    