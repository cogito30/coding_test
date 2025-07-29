# 시저 암호
def solution(s, n):
    answer = ''
    smallAlpha = "abcdefghijklmnopqrstuvwxyz"
    largeAlpha = smallAlpha.upper()
    for i in s:
        if i in smallAlpha:
            answer += smallAlpha[(ord(i) - ord('a') + n) % 26]
        elif i in largeAlpha:
            answer += largeAlpha[(ord(i) - ord('A') + n) % 26]
        else:
            answer += i
    return answer