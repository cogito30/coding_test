# 최소직사각형
def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0
    for size in sizes:
        w, h = max(size), min(size)
        if max_width <= w:
            max_width = w
        if max_height <= h:
            max_height = h
    answer = max_height * max_width
    return answer