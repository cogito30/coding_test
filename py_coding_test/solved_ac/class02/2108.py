# 통계학
## input()을 사용하거나 counter를 사용하지 않는 경우 시간초과. sys.stdin.readline과 counter를 동시에 사용하여야함
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num = int(input())
    num_list.append(num)

num_list.sort()
print(round(sum(num_list)/N))
print(num_list[N//2])

"""시간초과
count_num = []
for i in num_list:
    count_num.append((i, num_list.count(i)))
count_num.sort(key=lambda x: (x[1], x[0]))
"""
count_num = Counter(num_list).most_common()

if len(count_num) < 2:
    print(count_num[0][0])
elif count_num[0][1] == count_num[1][1]:
    print(count_num[1][0])
else:
    print(count_num[0][0])

print(num_list[-1] - num_list[0])