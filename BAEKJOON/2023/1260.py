# 백준 1260번  
# DFS와 BFS


from collections import deque

def DFS(visited, graph, idx, list):
    visited[idx] = 1
    list.append(idx)
    for i in graph[idx]:
        if(visited[i] == 0):
            DFS(visited, graph, i, list)

def BFS(visited, graph, start, list):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        v = queue.popleft()     # queue의 첫 번째 값 꺼내기
        list.append(v)
        for i in graph[v]:
            if(visited[i] == 0):
                queue.append(i)
                visited[i] = 1
            
N, M, V = map(int, input().split(" "))

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split(" "))
    if a not in graph[b]:
        graph[b].append(a)
    if b not in graph[a]:
        graph[a].append(b)

for i in range(N+1):
    graph[i] = sorted(graph[i])

visited = [0] * (N+1)
DFS_list = []
DFS(visited, graph, V, DFS_list)
for i in DFS_list:
    print(i,end=" ") 

print()

visited = [0] * (N+1)
BFS_list = []
BFS(visited, graph, V, BFS_list)
for i in BFS_list:
    print(i,end=" ") 