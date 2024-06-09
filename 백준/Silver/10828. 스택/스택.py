import sys
input = sys.stdin.readline
# stack -> First In Last Out
stack = []

N = int(input())

for i in range(N):
    command = input().split()
    
    if command[0] == 'push':
        stack.append(command[1])
    
    elif command[0] == 'pop':
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(stack))
    
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
        
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    