# 수 정렬하기 2
# pypy3로 제출. python 제출시 시간초과
N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

num_list.sort()
for i in num_list:
    print(i)