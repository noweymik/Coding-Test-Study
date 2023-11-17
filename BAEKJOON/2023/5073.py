# 백준 5073번
# 삼각형과 세 변

while True:
    x, y, z = map(int, input().split())
    if x==0 and y==0 and z==0:
        break
    
    if x==y and y==z:
        print("Equilateral")
    
    elif x==y or y==z or z==x:
        print("Isosceles")

    else:
        list = [x, y, z]
        list.sort(reverse=True)
        
        if list[0] >= (list[1] + list[2]):
            print("Invalid")
        else:
            print("Scalene")