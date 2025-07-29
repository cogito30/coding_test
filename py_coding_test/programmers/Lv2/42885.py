# 구명보트
def solution(people, limit):
    answer = 0
    people.sort()
    i, j = 0, len(people) - 1
    while True:
        if i > j:
            break
            
        if people[j] + people[i] <= limit:
            i += 1
            j -= 1
            answer += 1
        else: 
            j -= 1
            answer += 1
        
    return answer