# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    if len(my_str) % n == 0:
        for i in range(len(my_str)//n):
            answer.append(my_str[n*i:n*(i+1)])
    else:
        for i in range(len(my_str)//n + 1):
            answer.append(my_str[n*i:n*(i+1)])
    return answer