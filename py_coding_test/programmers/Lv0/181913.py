# 문자열 여러 번 뒤집기
def solution(my_string, queries):
    answer = ''
    for query in queries:
        my_string = my_string[:query[0]] + my_string[query[0]:query[1]+1][::-1] + my_string[query[1]+1:]
    answer = my_string
    return answer