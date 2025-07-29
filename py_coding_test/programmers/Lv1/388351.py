# 유연근무제
def solution(schedules, timelogs, startday):
    answer = 0
    N = len(schedules)
    for i in range(N):
        std_time = schedules[i]
        std_time_ten = schedules[i] + 10
        if std_time_ten % 100 >= 60:
            std_time_ten += 100
            std_time_ten -= 60
        if std_time_ten > 2400:
            std_time_ten = 2400
        count = 0
        start = startday - 1
        for time in timelogs[i]:
            start += 1
            if start == 6 or start == 7:
                continue
            if start > 7:
                start = 1
            if time <= std_time_ten:
                count += 1
            if count == 5:
                answer += 1
    return answer