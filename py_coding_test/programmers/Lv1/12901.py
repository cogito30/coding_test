# 2016년
def solution(a, b):
    answer = ''
    day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = 5 # FRI
    for i in range(a):
        total_day += month[i]
    total_day += b - 1
    answer = day[total_day % 7]
        
    return answer