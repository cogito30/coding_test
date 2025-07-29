# 소수 구하기
# 에라토스테네스의 체 사용
M, N = map(int, input().split())

primes = [True for _ in range(N+1)]
primes[0], primes[1] = False, False
for i in range(2, N+1):
    # 처리하지 않은 경우 시간초과
    if i ** 2 >= (N + 1):
        break
    if primes[i]:
        for num in range(2, i):
            if i % num == 0:
                primes[i] = False
                break
        for num in range(2*i, N+1, i):
            primes[num] = False

for i in range(M, N+1):
    if primes[i]:
        print(i)

"""시간초과
M, N = map(int, input().split())

primes = [True for _ in range(N+1)]
primes[0], primes[1] = False, False
for i in range(2, N+1):
    if primes[i]:
        for num in range(2, i):
            if i % num == 0:
                primes[i] = False
                break
        for num in range(2*i, N+1, i):
            primes[num] = False

for i in range(M, N+1):
    if primes[i]:
        print(i)
"""