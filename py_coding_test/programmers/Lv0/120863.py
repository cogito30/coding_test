# 다항식 더하기
def solution(polynomial):
    answer = ''
    polynomial = polynomial.split(" ")
    x_num = 0
    num = 0

    for i in polynomial:
        if "x" in i:
            if len(i) >= 2:
                print(i[:-1])
                x_num += int(i[:-1])
            else:
                x_num += 1
        elif i.isdecimal():
            num += int(i)

    if x_num > 1:
        answer += str(x_num) + "x"
    elif x_num > 0:
        answer += "x"
    if len(answer) > 0 and x_num > 0 and num > 0:
        answer += " + "
    if num > 0:
        answer += str(num)
    
    return answer