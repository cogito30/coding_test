# 추억 점수
def solution(name, yearning, photo):
    answer = []
    name_to_yearning = dict()
    
    for n, y in zip(name, yearning):
        name_to_yearning[n] = y
    
    for names in photo:
        num = 0
        for n in names:
            if name_to_yearning.get(n):
                num += name_to_yearning.get(n)
        answer.append(num)
    return answer