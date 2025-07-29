# 컨트롤 제트
def solution(s):
    answer = 0
    tmpNum = ""
    prevNum = 0
    for i in range(len(s)):
        if s[i].isdigit() or s[i] == "-":
            tmpNum += s[i]
        elif s[i] == "Z":
            answer -= prevNum
        elif len(tmpNum) > 0 and s[i] == " ":
            prevNum = int(tmpNum)
            answer += int(tmpNum)
            tmpNum = ""
        
        if i == len(s) - 1 and len(tmpNum) > 0:
            answer += int(tmpNum)
        
    return answer