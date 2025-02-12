import sys

input = sys.stdin.readline

n = int(input())

stack = []
output = ''
curr = 1
flag = 0
for i in range(n):
    num = int(input())
    
    while curr <= num:
        output += '+'
        stack.append(curr)
        curr += 1
    
    if stack[-1] == num:
        output += '-'
        stack.pop()
        
    else:
        print("NO")
        flag = 1
        break
        

if flag == 0:
    for o in output:
        print(o)