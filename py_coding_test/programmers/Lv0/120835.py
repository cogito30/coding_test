# 진료 순서 정하기
def solution(emergency):
    answer = []
    emergencyCopy = emergency[::]
    emergencyCopy.sort(reverse=True)
    
    for i in emergency:
        answer.append(emergencyCopy.index(i) + 1)
    return answer