# 배열 만들기 2
def solution(l, r):
    answer = []
    for j in range(l, r+1):
        s = str(j)
        for i in range(len(s)):
            if s[i] != "0" and s[i] != "5":
                break
            if i == len(s) - 1:
                answer.append(int(s))
    if len(answer) == 0:
        answer = [-1]
    return answer