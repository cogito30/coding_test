# 문자열 반복
T = int(input())
for _ in range(T):
    count, s = input().split()
    count = int(count)
    for i in s:
        print(i*count, end="")
    print()