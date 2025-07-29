# [PCCE 기출문제] 5번 / 심폐소생술
def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(5):
            if action == basic_order[i]:
                answer.append(i + 1)
    return answer