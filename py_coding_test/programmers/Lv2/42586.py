# 기능개발
def solution(progresses, speeds):
    answer = []
    # [96, 94], [3, 3], [2] 체크
    finish = []
    for i in range(len(progresses)):
        day = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] == 0:
            finish.append(day)
        else:
            finish.append(day+1)
    print(finish)
    maxDay = finish[0]
    count = 0
    for i in finish:
        if maxDay >= i:
            count += 1
        else:
            answer.append(count)
            maxDay = i
            count = 1
    answer.append(count)
    return answer