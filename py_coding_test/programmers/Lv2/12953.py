# N개의 최소공배수
import math
def solution(arr):
    answer = 0
    
    lcm_num = arr[0]
    for i in range(len(arr)):
        gcd_num = math.gcd(lcm_num, arr[i])
        lcm_num = lcm_num * arr[i] // gcd_num
    answer = lcm_num
    return answer