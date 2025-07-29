# 외계어 사전
def solution(spell, dic):
    answer = 2
    spell = set(spell)
    for word in dic:
        set_word = set([i for i in word])
        if set_word == spell:
            answer = 1
            break
    return answer