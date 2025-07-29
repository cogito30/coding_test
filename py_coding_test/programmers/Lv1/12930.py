# 이상한 문자 만들기
def solution(s):
    answer = ''
    start = 1
    for i in range(1, len(s)+1):
        if s[i-1].isalpha():
            if start % 2 == 1:
                answer += s[i-1].upper()
            else:
                answer += s[i-1].lower()
            start += 1
        else:
            start = 1
            answer += " "
    return answer