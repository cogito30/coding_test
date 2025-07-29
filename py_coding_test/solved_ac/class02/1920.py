# 수 찾기
N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)

"""시간초과
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)
"""