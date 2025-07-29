# solved.ac
# python의 round는 오사오입으로 5 초과일 경우 올림
# input() 사용시 시간초과 sys.stdin.readline 사용
import sys
input = sys.stdin.readline

def new_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    
n = int(input())

if n == 0:
    print(0)
else:
    rates = []
    for _ in range(n):
        rate = int(input())
        rates.append(rate)

    rates.sort()
    exclude_num = new_round(n*0.15)
    if exclude_num == 0:
        print(new_round(sum(rates)/n))
    else:
        total_score = sum(rates[exclude_num:-exclude_num])
        len_rates = len(rates[exclude_num:-exclude_num])
        print(new_round(total_score/len_rates))