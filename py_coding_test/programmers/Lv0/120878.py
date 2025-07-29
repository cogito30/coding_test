# 유한소수 판별하기
import math

def solution(a, b):
    answer = 1
    gcd = math.gcd(a, b)
    b //= gcd
    prime_list = set()
    n = b
    
    for i in range(2, n + 1):
        while b  % i == 0:
            b //= i
            prime_list.add(i)

    for i in prime_list:
        if i != 2 and i != 5:
            answer = 2
            break
    return answer