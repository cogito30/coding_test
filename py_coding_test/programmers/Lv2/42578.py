# 의상
def solution(clothes):
    answer = 1
    clothMap = {}
    for cloth in clothes:
        if clothMap.get(cloth[1], None):
            clothMap[cloth[1]] += 1
        else:
            clothMap[cloth[1]] = 1
    for k, v in clothMap.items():
        answer *= (v+1)
    answer -= 1
    return answer