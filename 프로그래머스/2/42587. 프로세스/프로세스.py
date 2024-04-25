def solution(priorities, location):
    answer = 0
    queue =  [(i,p) for i,p in enumerate(priorities)] 
    
    while queue:
        process = queue.pop(0)
        # queue에 있는 프로세스 중에 현재 process 보다 더 높은 우선 순위가 있는 경우
        # process[1], q[1]은 우선순위 수
        if any(process[1] < q[1] for q in queue):
            queue.append(process)
        # queue에 있는 어떤 프로세스 보다 우선순위가 높을 경우 pop (실행) -> answer += 1 (실행한 프로세스 개수)
        # 만약 현재 실행한 process가 우리가 찾으려는 위치의 프로세스라면 몇 번째로 실행됐는지 answer 리턴하기
        else:
            answer += 1
            if process[0] == location:
                return answer 
