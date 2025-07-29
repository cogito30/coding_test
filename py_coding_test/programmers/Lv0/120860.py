# 직사각형 넓이 구하기
def solution(dots):
    answer = 0
    xList = []
    yList = []
    for x, y in dots:
        xList.append(x)
        yList.append(y)
    minX, maxX = min(xList), max(xList)
    minY, maxY = min(yList), max(yList)
    
    answer = (maxX - minX) * (maxY - minY)
        
    return answer