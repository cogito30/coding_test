# 명예의 전당(1)
def solution(k, score):
    answer = []
    honor_list = []
    for i in range(len(score)):
        if len(honor_list) < k:
            honor_list.append(score[i])
        elif score[i] >= honor_list[0]:
            honor_list.pop(0)
            honor_list.append(score[i])
        honor_list.sort()
        answer.append(honor_list[0]) 
    return answer