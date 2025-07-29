# 균형잡힌 세상
# [(]) 주의
# )(를 고려
while True:
    sentance = input()
    if sentance == ".":
        break
    stack = []
    for i in sentance:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if len(stack) > 0 and stack.pop() == "(":
                continue
            else:
                stack = [-1]
                break
        elif i == "]":
            if len(stack) > 0 and stack.pop() == "[":
                continue
            else:
                stack = [-1]
                break

    if len(stack) > 0:
        print("no")
    else:
        print("yes")

"""
while True:
    line = input()
    
    if line == '.':
        break
    
    stack = []
    for i in line:
        if i in "[(":
            stack.append(i)
        elif i == "]":
            if not stack or stack.pop() != "[":
                print('no')
                break
        elif i == ")":
            if not stack or stack.pop() != "(":
                print('no')
                break
        elif i =='.':
            if stack:
                print('no')
            else:
                print('yes')

"""