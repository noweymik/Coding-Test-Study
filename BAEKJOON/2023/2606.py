# 백준 2606번  
# 바이러스
# 배운 점 : DFS

n = int(input())
networks = int(input())
graph = [[] for i in range(n+1)]

for i in range(networks):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (n+1)

def DFS(index):
    visited[index] = 1
    
    for i in graph[index]:
        if visited[i] == 0:
            DFS(i)

DFS(1)
print(sum(visited)-1)

