# [21년 재직자 대회 예선] 전광판
import sys

# 숫자별 전구 켜짐 표시: 0일 경우 [1, 1, 1, 0, 1, 1, 1]
def check_led(num):
    led = [0 for _ in range(7)]
    if num < 0:
        led = [0, 0, 0, 0, 0, 0, 0]
    elif num == 0:
        led = [1, 1, 1, 0, 1, 1, 1]
    elif num == 1:
        led = [0, 0, 1, 0, 0, 0, 1]
    elif num == 2:
        led = [0, 1, 1, 1, 1, 1, 0]
    elif num == 3:
        led = [0, 1, 1, 1, 0, 1, 1]
    elif num == 4:
        led = [1, 0, 1, 1, 0, 0, 1]
    elif num == 5:
        led = [1, 1, 0, 1, 0, 1, 1]
    elif num == 6:
        led = [1, 1, 0, 1, 1, 1, 1]
    elif num == 7:
        led = [1, 1, 1, 0, 0, 0, 1]
    elif num == 8:
        led = [1, 1, 1, 1, 1, 1, 1]
    elif num == 9:
        led = [1, 1, 1, 1, 0, 1, 1]
    return led

def diff_led(led1, led2):
    diff_count = 0
    for i in range(7):
        if led1[i] != led2[i]:
            diff_count += 1
    return diff_count

T = int(input())
for t in range(T):
    A, B = map(int, input().split())

    answer = 0
    while A > 0 or B > 0:
        if A < 0:
            A_left = -1
        else:
            A_left = A%10
        if B < 0:
            B_left = -1
        else:
            B_left = B%10
        
        A_led = check_led(A_left)
        B_led = check_led(B_left)
        answer += diff_led(A_led, B_led)
        
        if A >= 10:
            A //= 10
        elif A >= 0 and A < 10:
            A = -1
        if B >= 10:
            B //= 10
        elif B >= 0 and B < 10:
            B = -1

    print(answer)