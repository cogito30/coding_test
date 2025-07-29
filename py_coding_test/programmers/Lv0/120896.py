# 한 번만 등장한 문자
def solution(s):
    answer = ''
    countAlpha = {}
    alphaList = []
    for i in s:
        if countAlpha.get(i):
            countAlpha[i] += 1
        else:
            countAlpha[i] = 1
    for k, v in countAlpha.items():
        if v == 1:
            alphaList.append(k)
    alphaList.sort()
    answer = ''.join(alphaList)
    return answer