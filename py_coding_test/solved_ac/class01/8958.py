# OX퀴즈
T = int(input())
for _ in range(T):
    states = input()
    score = 0
    total_score = 0
    for s in states:
        if s == 'O':
            score += 1
            total_score += score
        elif s == 'X':
            score = 0
    print(total_score)