# 소수 찾기
N = int(input())
num_list = list(map(int, input().split()))
# 1, 2일 경우 확인
answer = 0
for num in num_list:
    if num == 2:
        answer += 1
    for i in range(2, num):
        if num % i == 0:
            break
        elif i == num - 1:
            answer += 1
print(answer)