# 종이 자르기
def solution(M, N):
    answer = 0
    answer = min((M*(N-1) + M-1), (N*(M-1) + N-1))
    return answer