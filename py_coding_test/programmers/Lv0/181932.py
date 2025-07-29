# 코드 처리하기
def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if i % 2 == 0 and code[i] != "1":
                answer += code[i]
            elif code[i] == "1":
                mode = 1
        elif mode == 1:
            if i % 2 == 1 and code[i] != "1":
                answer += code[i]
            elif code[i] == "1":
                mode = 0
    if len(answer) == 0:
        answer = "EMPTY"
    return answer