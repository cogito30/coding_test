# 스택
# input으로 했을 경우 시간초과, sys.stdin.readline 사용 혹은 pypy3 사용
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    line = input().split()
    if line[0] == "push":
        stack.append(line[1])
    elif line[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif line[0] == "size":
        print(len(stack))
    elif line[0] == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif line[0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
