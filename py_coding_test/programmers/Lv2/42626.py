# 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        if len(scoville) == 0:
            answer = -1
            break
        answer += 1
        min2 = heapq.heappop(scoville)
        newScoville = min1 + min2 * 2
        heapq.heappush(scoville, newScoville)

    return answer
