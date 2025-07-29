# 올바른 괄호
def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                answer = False
                break
            elif stack.pop() == "(":
                continue
            else:
                answer = False
                break
    if len(stack) != 0:
        answer = False
    return answer