# X보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split()))

for num in A:
    if num < X:
        print(num, end=" ")
