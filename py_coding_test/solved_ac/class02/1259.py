# 팰린드롬수
while True:
    num = input()
    if num == '0':
        break
    if num[::-1] == num:
        print('yes')
    else:
        print('no')