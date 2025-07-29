# 프로세스
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    priorityList = sorted(priorities, reverse=True)
    for idx, priority in enumerate(priorities):
        queue.append((priority, idx))
    print(priorityList)
    for i in priorityList:
        answer += 1
        while True:
            if queue[0][0] == i:
                if queue[0][1] == location:
                    return answer
                queue.popleft()
                break
            else:
                queue.rotate(-1)
