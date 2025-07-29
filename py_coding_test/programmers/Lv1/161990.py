# 다른 사람의 풀이
def solution(wallpaper):
    answer = []
    row_position = []
    col_position = []
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[row])):
            if wallpaper[row][col] == "#":
                row_position.append(row)
                col_position.append(col)
    answer = [min(row_position), min(col_position), max(row_position) + 1, max(col_position) + 1]

    return answer