def dfs(hp, dungeons, visited, count):    
    global answer
    
    # 1) 지금까지 최대 갱신
    answer = max(answer, count)
    
    # 2) 다음 분기
    for i in range(len(dungeons)):
        req, cost = dungeons[i]
        
        if not visited[i] and hp >= req:
            visited[i] = True
            dfs(hp-cost, dungeons, visited, count+1)
            visited[i] = False    
            

def solution(k, dungeons):    
    global answer
    answer = 0
    visited = [False] * len(dungeons)        
    dfs(k, dungeons, visited, 0)
        
    return answer