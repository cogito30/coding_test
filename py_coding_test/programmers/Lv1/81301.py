# 숫자 문자열과 영단어
def solution(s):
    answer = ""
    alpha_to_num= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    
    start = 0
    for i in range(1, len(s) + 1):
        if s[i-1].isdecimal():
            start = i
            answer += str(s[i-1])
            continue
        if s[start:i+1] in alpha_to_num:
            answer += str(alpha_to_num.index(s[start:i+1]))
            start = i+1
            
    answer = int(answer)
    return answer