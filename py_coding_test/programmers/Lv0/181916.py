# 주사위 게임 3
def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    dice.sort()
    if dice[0] == dice[3]:
        answer = dice[0] * 1111
    elif dice[0] == dice[2] and dice[2] != dice[3]:
        answer = (dice[0]*10 + dice[3]) ** 2
    elif dice[1] == dice[3] and dice[0] != dice[1]:
        answer = (dice[3]*10 + dice[0]) ** 2
    elif dice[0] == dice[1] and dice[1] != dice[2] and dice[2] == dice[3]:
        answer = (dice[0] + dice[3]) * abs(dice[0] - dice[3])
    elif dice[0] == dice[1] and dice[1] != dice[2] and dice[2] != dice[3]:
        answer = dice[2] * dice[3]
    elif dice[1] == dice[2] and dice[0] != dice[1] and dice[2] != dice[3]:
        answer = dice[0] * dice[3]
    elif dice[2] == dice[3] and dice[0] != dice[1] and dice[1] != dice[2]:
        answer = dice[0] * dice[1]
    else:
        answer = dice[0]
    return answer