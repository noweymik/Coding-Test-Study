def solution(brown, yellow):
    total = brown + yellow
    # 가로 width 세로 height
    
    for height in range(1, total+1):
        if total % height == 0:            
            width = int(total / height)
            
            if width >= height:
                # width*height - (width-2)*(height-2) = 전체 - yellow = brown
                if 2*(width) + 2*(height) - 4 == brown:
                    return [width, height]    