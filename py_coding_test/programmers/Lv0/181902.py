# 문자 개수 세기
def solution(my_string):
    answer = 0
    lower_alpha = [0 for _ in range(26)]
    upper_alpha = [0 for _ in range(26)]
    for i in my_string:
        if i.isupper():
            upper_alpha[ord(i) - ord('A')] += 1
        else:
            lower_alpha[ord(i) - ord('a')] += 1
            
    answer = upper_alpha + lower_alpha
    return answer