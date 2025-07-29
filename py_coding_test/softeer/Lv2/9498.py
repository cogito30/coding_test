# [한양대 HCPC 2023] Yeah, but How?
import sys

S = input()

stack = []
for idx, i in enumerate(S):
    if i == '(':
        stack.append(i)
    elif i == ')':
        stack.append('1')
        stack.append(i)
        if idx != len(S) - 1:
            stack.append('+')
answer = ''.join(stack)
print(answer)