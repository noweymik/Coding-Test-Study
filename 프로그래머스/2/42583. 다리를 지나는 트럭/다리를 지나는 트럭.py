from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    # pop(0) -> O(N)이지만 popleft() -> O(1) 
    # 그래서 deque 사용
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    total_weights = 0
    while bridge:
        time += 1
        total_weights -= bridge.popleft()
        
        if truck_weights:
            # bridge에 있는 무게와 대기 트럭 첫번째 무게 합친게 weight 이내일 때
            if total_weights + truck_weights[0] <= weight:  
                total_weights += truck_weights[0]
                bridge.append(truck_weights.popleft())    
            # bridge list 끝 쪽에 0 삽입 
            else:
                bridge.append(0)
    
    return time