# 집합
## line[1]을 숫자가 아닌 문자열로 처리할 경우 통과하지 못함
import sys
input = sys.stdin.readline
M = int(input())
S = set()
for _ in range(M):
    line = input().split()
    if len(line) == 1:
        if line[0] == "all":
            S = set(range(1, 21))
        elif line[0] == "empty":
            S = set()
    else:
        line[1] = int(line[1])
        if line[0] == "add":
            S.add(line[1])
        elif line[0] == "remove":
            S.discard(line[1])
        elif line[0] == "check":
            if line[1] in S:
                print(1)
            else:
                print(0)
        elif line[0] == "toggle":
            if line[1] in S:
                S.remove(line[1])
            else:
                S.add(line[1])

