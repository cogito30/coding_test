# 최소 힙
# input() 사용시 시간초과, sys.stdin.readline 사용
import heapq
import sys
input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)



        import heapq

""" print가 아닌 result를 만들어 처리하고 pypy3 사용시 시간초과 없음
# 최소 힙
import heapq
N = int(input())
heap = []
result = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, x)

for i in result:
    print(i)
"""