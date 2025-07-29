# 3진법 뒤집기
def solution(n):
    answer = 0
    threeList = []
    while n > 0:
        threeList.append(n%3)
        n //= 3
    threeList.reverse()
    for idx, elem in enumerate(threeList):
        answer += 3**(idx) * elem
    return answer