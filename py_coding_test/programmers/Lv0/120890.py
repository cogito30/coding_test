# 가까운 수
def solution(array, n):
    # 처음에 원소 반드시 넣어 줄 것
    answer = array[0]
    diff = max(array)
    for i in array:
        if diff > abs(n - i):
            diff = abs(n - i)
            answer = i
        elif diff == abs(n - i):
            if answer > i:
                answer = i
    return answer