# 설탕 배달
N = int(input())

three_count = 0
five_count = N // 5
N %= 5
three_count = N // 3
N %= 3
while True:
    if N == 0:
        break
    elif five_count < 0:
        break
    else:
        five_count -= 1
        N += 5
    three_count += N // 3
    N %= 3

if five_count < 0:
    print(-1)
else:
    print(five_count + three_count)

"""
N = int(input())
cnt = 0
while(N>0):
    if(N%5==0):
        cnt += N//5 
        break
    else:
        N -= 3
        cnt += 1
if (N<0):
    print(-1)
else:
    print(cnt)
"""