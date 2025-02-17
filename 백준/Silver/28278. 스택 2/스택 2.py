import sys
input = sys.stdin.readline

stack = []

N = int(input())

for i in range(N):
    cmd = input()    
    if cmd[0] == '1':        
        cmd_line = cmd.split()    
        stack.append(int(cmd_line[1]))
    elif cmd[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == '3':
        print(len(stack))
    elif cmd[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)