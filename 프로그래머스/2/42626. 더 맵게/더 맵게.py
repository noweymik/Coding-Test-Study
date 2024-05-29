import heapq as hp

def solution(scoville, K):
    answer = 0
    hp.heapify(scoville)    
    
    while True:
        # scoville의 최솟값이 K보다 작다면 섞는 과정을 거쳐야함
        if scoville[0] < K:          
            if len(scoville) >= 2:
                a = hp.heappop(scoville)
                b = hp.heappop(scoville)
                hp.heappush(scoville, a + b*2)
                answer += 1
            else: # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
                return -1
        # scoville의 최솟값이 K보다 큰 경우 (끝!)
        else: 
            return answer    
        
    return answer