import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    stack = []    
    line = input()
    
    for l in line:
        if l == '(':
            stack.append(l)
        elif l == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else: 
        if not stack:
            print("YES")
        else:
            print("NO")