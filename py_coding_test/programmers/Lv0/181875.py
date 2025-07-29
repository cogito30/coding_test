# 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    answer = []
    for idx, word in enumerate(strArr):
        if idx % 2 == 0:
            answer.append(word.lower())
        else:
            answer.append(word.upper())
    return answer