# 기사단원의 무기
def count_num(num):
    count = 0
    for i in range(1, num+1):
        if i * i == num:
            count += 1
        elif i * i > num:
            break
        elif num % i == 0:
            count += 2
    return count

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        weapon = count_num(i)
        if weapon > limit:
            answer += power
        else:
            answer += weapon
    
    return answer