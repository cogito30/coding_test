# 소수 찾기
def is_prime(num):
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True
            
def solution(n):
    answer = 0
    primes = [True for _ in range(n+1)]
    for i in range(2, n+1):
        if primes[i]:
            if is_prime(i):
                for j in range(2*i, n+1, i):
                    primes[j] = False
    answer = sum(primes) - 2
    return answer