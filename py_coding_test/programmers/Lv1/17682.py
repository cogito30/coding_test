# [1차] 다트 게임
def solution(dartResult):
    answer = 0
    bonus = ["S", "D", "T"]
    option = ["*", "#"]
    score_list = []
    str_num = ""
    for i in range(len(dartResult)):
        if dartResult[i].isdecimal():
            str_num += dartResult[i]
        elif dartResult[i] in bonus:
            num = int(str_num)
            index = bonus.index(dartResult[i])
            score_list.append(num ** (index + 1))
            str_num = ""
        elif dartResult[i] in option:
            if dartResult[i] == option[1]:
                score_list[-1] *= -1
            elif dartResult[i] == option[0]:
                score_list[-1] *= 2
                if len(score_list) >= 2:
                    score_list[-2] *= 2
    answer = sum(score_list)
    print(score_list)
            
        
    return answer