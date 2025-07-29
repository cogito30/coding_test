# 타겟 넘버
from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append((0, 0))  # (index, 현재 합계)
    count = 0

    while queue:
        index, current_sum = queue.popleft()
        if index == len(numbers):
            if current_sum == target:
                count += 1
        else:
            queue.append((index + 1, current_sum + numbers[index]))  # '+' 경우
            queue.append((index + 1, current_sum - numbers[index]))  # '-' 경우

    return count

"""
def solution(numbers, target):
    answer = 0
    def dfs(i, currentSum):
        if i == len(numbers):
            if currentSum == target:
                return 1
            else:
                return 0
        plus = dfs(i + 1, currentSum + numbers[i])
        minus = dfs(i + 1, currentSum - numbers[i])
        return plus + minus
    answer = dfs(0, 0)
    return answer
"""

"""
def solution(numbers, target):
    # DFS와 nonlocal 활용
    
    answer = 0
    def dfs(i, totalSum):
        nonlocal answer
        if i == (len(numbers)):
            if totalSum == target:
                answer += 1
                return
        else:
            dfs(i+1, totalSum + numbers[i])
            dfs(i+1, totalSum - numbers[i])
    dfs(0, 0)
    return answer
"""