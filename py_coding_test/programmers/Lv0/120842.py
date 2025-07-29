# 2차원으로 만들기
def solution(num_list, n):
    answer = []
    for idx, num in enumerate(num_list):
        if idx % n == 0:
            answer.append([])
        answer[-1].append(num)
        
    return answer