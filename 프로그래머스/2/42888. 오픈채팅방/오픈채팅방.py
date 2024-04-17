def solution(record):
    answer = []   # result 담을 리스트
    userId = {}   # userId와 nickname을 담을 dict
    
    for r in record:
        line = r.split(" ")
        command = line[0]
        id = line[1]

        # Enter or Change면 userId의 key의 value 추가 또는 업데이트
        if command == 'Enter' or command == 'Change':            
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
