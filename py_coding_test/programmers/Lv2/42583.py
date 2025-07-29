# 다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = deque()
    totalBridge = truck_weights[0]
    onBridge.append((truck_weights[0], 1))
    truck_weights.pop(0)
    while len(onBridge) > 0:
        if (answer - onBridge[0][1]) >= bridge_length:
            totalBridge -= onBridge.popleft()[0]
        if len(truck_weights) > 0 and (truck_weights[0] + totalBridge) <= weight:
            totalBridge += truck_weights[0]
            onBridge.append((truck_weights[0], answer))
            truck_weights.pop(0)
        answer += 1
    return answer - 1