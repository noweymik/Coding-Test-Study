# 백준 11725번
# 트리의 부모 찾기
# 배운 점 : 
# 1) setrecursionlimit
#    재귀함수 사용하는 문제에 꼭 사용하기...
# 2) input() 대신 sys.stdin.readline()
#    반복문으로 여러줄을 입력 받아야 할 때는 input()으로 입력 받는다면 시간초과가 발생할 수 있음
#    기능상 큰 차이가 없지만 속도 차이가 큼
#    맨 위에 input = sys.stdin.readline 선언해서 사용하기 ㅎㅎ

import sys
input=sys.stdin.readline

# recursion 호출 개수 제한
sys.setrecursionlimit(10**6)

def DFS(graph, v, parent):
    
    #현재 노드와 연결된 노드를 재귀적으로 호출
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
            DFS(graph, i, parent)

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

DFS(graph, 1, parent)

for n in range(2, N+1):
    print(parent[n])