# [PCCP 기출문제] 1번/붕대 감기
def solution(bandage, health, attacks):
    answer = 0
    max_time = attacks[-1][0]
    max_health = health
    i = 0
    success = 0
    for time in range(1, max_time + 1):
        
        if attacks[i][0] == time:
            health -= attacks[i][1]
            i += 1
            success = 0
        else:
            health += bandage[1]
            success +=1
        
        if success == bandage[0]:
            success = 0
            health += bandage[2]
            
        if health > max_health:
            health = max_health

        if health <= 0:
            break
    if health <= 0:
        answer = -1
    else:
        answer = health
    return answer