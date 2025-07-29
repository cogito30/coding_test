# 이진수 더하기
def solution(bin1, bin2):
    answer = ''
    answer = int(bin1, 2) + int(bin2, 2)
    answer = str(bin(answer))[2:]
    return answer