# 개수 세기
N = int(input())
arr = list(map(int, input().split()))
v = int(input())

answer = 0
for num in arr:
    if num == v:
        answer += 1
print(answer)