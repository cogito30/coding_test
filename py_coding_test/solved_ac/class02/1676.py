# 팩토리얼 0의 개수
N = int(input())

fac = 1
for i in range(1, N+1):
    fac *= i

answer = 0
fac = str(fac)[::-1]
for i in range(len(fac)):
    if fac[i] == '0':
        answer += 1
    else:
        break

print(answer)

"""
def fac(num):
    if num<=1:
        return 1
    return fac(num-1)*num

N = int(input())
result = 0
N = fac(N)

while True:
    if (N%10 == 0):
        result += 1
        N //= 10
    else:
        print(result)
        break
"""