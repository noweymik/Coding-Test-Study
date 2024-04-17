def solution(record):
    answer = []   # result 담을 리스트
    userId = {}   # userId와 nickname을 담을 dict
    
    for r in record:
        line = r.split(" ")
        command = line[0]
        id = line[1]
        
        # command 가 Enter라면 userId[id] 추가 또는 업데이트
        if command == 'Enter':            
            userId[id] = line[2]
        
        elif command == 'Change':
            if id in userId:
                userId[id] = line[2]
        
    for r in record:
        line = r.split(" ")
        command = line[0]
        id = line[1]
        
        if command == 'Enter':  
            answer.append(userId[id]+"님이 들어왔습니다.")
        elif command == 'Leave':
            answer.append(userId[id]+"님이 나갔습니다.")
        
    return answer