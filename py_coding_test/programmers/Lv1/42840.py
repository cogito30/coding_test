# 모의고사
def solution(answers):
    answer = []
    first_student = [1,2,3,4,5]
    second_student = [2,1,2,3,2,4,2,5]
    third_student = [3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == first_student[i%5]:
            scores[0] +=1 
        if answers[i] == second_student[i%8]:
            scores[1] +=1 
        if answers[i] == third_student[i%10]:
            scores[2] +=1 

    max_score = max(scores)
    for i in range(len(scores)):
        if scores[i] == max_score:
            answer.append(i+1)
    return answer