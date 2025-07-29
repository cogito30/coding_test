# 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
total = A * B * C
total_str = str(total)
for i in range(10):
    print(total_str.count(str(i)))