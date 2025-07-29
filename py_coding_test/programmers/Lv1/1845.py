# 폰켓몬
def solution(nums):
    answer = 0
    lenNums = len(nums) // 2
    lenSet = len(set(nums))
    if lenSet < lenNums:
        answer = lenSet
    else:
        answer = lenNums
    return answer