# 백준 20920번
# 영단어 암기는 괴로워

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

vocab_dict = {}

for i in range(N):
    word = input().rstrip()
    
    if len(word) >= M:
        if word not in vocab_dict:
            vocab_dict[word] = 1
        else:
            vocab_dict[word] += 1

# item : 조건 1,2,3             
vocab_dict = dict(sorted(vocab_dict.items(), \
                key=lambda item: (-item[1], -len(item[0]), item[0])))

for v in vocab_dict:
    print(v)