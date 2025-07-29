# 뒤에서 5등까지
def solution(num_list):
    answer = []
    num_list.sort()
    answer = num_list[:5]
    return answer