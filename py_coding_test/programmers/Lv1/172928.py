# 공원 산책
def solution(park, routes):
    answer = []
    row_len = len(park)
    col_len = len(park[0])
    direction = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
    cur_r = 0
    cur_c = 0
    for i in range(row_len):
        for j in range(col_len):
            if park[i][j] == "S":
                cur_r, cur_c = i, j
                
    for i in routes:
        dr = direction[i[0]][0]
        dc = direction[i[0]][1]
        for j in range(int(i[2])):
            nr = cur_r + dr*(j+1)
            nc = cur_c + dc*(j+1)
            if nr < 0 or nc < 0 or nr >= row_len or nc >= col_len:
                break
            if park[nr][nc] == "X":
                break
            if j == int(i[2]) - 1:
                cur_r = nr
                cur_c = nc
    answer = [cur_r, cur_c]
    return answer