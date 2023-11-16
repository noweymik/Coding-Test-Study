# 백준 4659번
# 비밀번호 발음하기

def func (word):
    total_v_count = 0
    v_count = 0         # 연속된 모음 수
    c_count = 0         # 연속된 자음 수
    prev = "?"
    
    for w in word:
        print(w)
            
        if w in ['a','e','i','o','u']:
            v_count += 1
            total_v_count += 1
            c_count = 0
            
        elif w not in ['a','e','i','o','u']:
            c_count += 1
            v_count = 0
        
        if v_count >= 3 or c_count >= 3:
            print("<" + word + "> is not acceptable.")
            return
        
        if prev == w and w not in ['e', 'o']:
            print("<" + word + "> is not acceptable.")
            return 
        
        prev = w
        
    if total_v_count < 1:
        print("<" + word + "> is not acceptable.")
    else:
        print("<" + word + "> is acceptable.")        
        
while True:    
    input_str = input()
    if input_str == "end":
        break
    else:
        func(input_str)