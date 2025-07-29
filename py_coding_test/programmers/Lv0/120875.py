# 평행
def solution(dots):
    answer = 0
    dots.sort()
    line1 = (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0]) 
    line2 = (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0])
    if line1 == line2:
        answer = 1
    else:
        answer = 0
    return answer