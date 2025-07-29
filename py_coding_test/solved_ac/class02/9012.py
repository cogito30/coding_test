# 괄호
T = int(input())
for _ in range(T):
    s = input()
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) > 0 and stack.pop() == "(":
                continue
            else:
                answer = False
                break
    # "(("인 경우 주의
    if answer and len(stack) == 0:
        print("YES")
    else:
        print("NO")

"""
T = int(input())
for _ in range(T):
    data = input()
    cnt = 0
    for i in data:
        if i =='(':
            cnt += 1
        elif i == ')':
            if cnt > 0:
                cnt -= 1
            else:
                cnt -= 1
                break
    if cnt == 0:
        print('YES')
    else:
        print('NO')
"""