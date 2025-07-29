# 중복된 문자 제거
def solution(my_string):
    answer = my_string[0]
    for i in range(len(my_string)):
        for j in range(i):
            if my_string[i] == my_string[j]:
                break
            elif j == i - 1:
                answer += my_string[i]
                
    return answer