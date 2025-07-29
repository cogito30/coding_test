# 특이한 정렬
def solution(numlist, n):
    answer = []
    numlist.sort(key = lambda x: (abs(n-x), -x))
    answer = numlist
    return answer