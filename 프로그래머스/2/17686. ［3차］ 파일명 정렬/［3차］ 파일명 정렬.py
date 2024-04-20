def solution(files):
    answer = []
    file_dict = {}
    
    for name in files:
        head = number = tail = ""
        # head        
        for index, s in enumerate(name): 
            if s.isdigit() is False:
                head += s
            else:
                break
        # number 
        for i in range(index, len(name)):               
            if name[i].isdigit() is True:
                number += name[i]
                index += 1
            else:
                break
        # tail        
        for i in range(index, len(name)):
            tail += name[i]
        
        # append to dictionary
        file_dict[name] = [head, number, tail]
    
    # 1번째 정렬 기준 : 대소문자 구분없이(lower 사용) head, 2번째 정렬 기준 : number
    sorted_dict = {key: file_dict[key] for key in sorted(file_dict, key=lambda k: (file_dict[k][0].lower(), int(file_dict[k][1])))}
    
    for file_name in sorted_dict:
        answer.append(file_name)
        
    return answer