# 최대공약수와 최소공배수
import math
A, B = map(int, input().split())

gcd_num = math.gcd(A, B)
lcm_num = (A * B) // gcd_num

print(gcd_num)
print(lcm_num)