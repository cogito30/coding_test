# 그림 확대
def solution(picture, k):
    answer = []
    for i in picture:
        pixel = ""
        for j in i:
            pixel += j * k
        for _ in range(k):
            answer.append(pixel)
        
    return answer