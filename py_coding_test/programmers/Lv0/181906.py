# 접두사인지 확인하기
def solution(my_string, is_prefix):
    answer = 0
    if is_prefix == my_string[:len(is_prefix)]:
        answer = 1
    else:
        answer = 0
    return answer