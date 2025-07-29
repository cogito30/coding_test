# 큐
## 시간 초과이므로 pypy3사용 혹은 sys.stdin.readline 사용
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dq = deque()
for _ in range(N):
    line = input().split()
    if line[0] == "push":
        dq.append(line[1])
    elif line[0] == "pop":
        if len(dq) > 0:
            print(dq.popleft())
        else:
            print(-1)
    elif line[0] == "size":
        print(len(dq))
    elif line[0] == "empty":
        if len(dq) > 0:
            print(0)
        else:
            print(1)
    elif line[0] == "front":
        if len(dq) > 0:
            print(dq[0])
        else:
            print(-1)
    elif line[0] == "back":
        if len(dq) > 0:
            print(dq[-1])
        else:
            print(-1)