# [21년 재직자 대회 예선] 비밀 메뉴
import sys

M, N, K = map(int, input().split())
secret_recipe = list(map(int, input().split()))
control = list(map(int, input().split()))

answer = "normal"
if len(secret_recipe) > len(control):
    answer = "normal"
else:
    for i in range(N-M+1):
        for j in range(M):
            if secret_recipe[j] != control[i+j]:
                break
            if j == M - 1:
                answer = "secret"
            
print(answer)