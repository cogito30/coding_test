# 분수의 덧셈
import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = denom1 * denom2
    numer = numer1*denom2 + numer2*denom1
    
    gcd_num = math.gcd(numer, denom)
    answer = [numer//gcd_num, denom//gcd_num]
    print(numer)
    return answer