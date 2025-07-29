# 가까운 1 찾기
def solution(arr, idx):
    answer = -1
    for i, ele in enumerate(arr):
        if i >= idx and ele == 1:
            answer = i
            break
    return answer