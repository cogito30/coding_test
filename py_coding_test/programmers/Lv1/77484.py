# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = []
    win_count = 0
    random_count = 0
    for i in lottos:
        if i in win_nums:
            win_count += 1
        elif i == 0:
            random_count += 1
    max_rank = min(7 - random_count - win_count, 6) 
    min_rank = min(7 - win_count, 6)
    answer = [max_rank, min_rank]
    return answer