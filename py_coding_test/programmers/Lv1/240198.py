# [PCCE 기출문제] 10번 / 공원
def solution(mats, park):
    answer = -1
    M, N = len(park), len(park[0])
    mats.sort(reverse=True)
    
    def check(r, c, size):
        if r + size > M or c + size > N:
            return False
        for i in range(r, r + size):
            for j in range(c, c + size):
                if park[i][j] != "-1":
                    return False
        return True
    
    for mat in mats:
        for row in range(M):
            for col in range(N):
                if check(row, col, mat):
                    return mat
    return answer