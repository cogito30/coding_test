# 옹알이 (1)
def solution(babbling):
    answer = 0
    cousin = ["aya", "ye", "woo", "ma"]

    for babble in babbling:
        start = 0
        for i in range(1, len(babble) + 1):
            if babble[start:i] in cousin:
                start = i

        if start == len(babble):
            answer += 1

    return answer