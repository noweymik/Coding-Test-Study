import sys
input = sys.stdin.readline

string = input().strip()

str_dict = {}
for i in range(len(string)):
    str_dict[string[i]] = 0
for s in string:
    str_dict[s] += 1

str_dict = dict(sorted(str_dict.items()))   # 먼저 sort 해주기

# 팰린드롬 가능한 조건
# 1. 모든 알파벳이 짝수일 경우
# 2. 한 개의 알파벳만 홀수 개일 경우 (나머지 짝수)
# AAAABBC -> AAB C BAA
odd = []
for k, v in str_dict.items():
    if v % 2 == 1:
        odd.append(k)

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    output = ''
    for k, v in str_dict.items():
        output += k * (v // 2) # 반쪽짜리만 먼저 만들기
        
    if odd:
        output += odd[0] + output[::-1]
    else:
        output += output[::-1]

    print(output)