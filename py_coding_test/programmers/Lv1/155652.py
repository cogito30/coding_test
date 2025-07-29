# 둘만의 암호
def solution(s, skip, index):
    answer = ''
    s_list = [i for i in s]
    skip_list = [i for i in skip]
    alpha_list = []
    
    for i in range(26):
        alpha = chr(ord('a') + i)
        if alpha not in skip_list:
            alpha_list.append(alpha)
    for i in s_list:
        idx = alpha_list.index(i)
        answer += alpha_list[(idx + index)%len(alpha_list)]

    return answer