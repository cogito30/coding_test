# 가장 큰 수
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    # [0, 0], 0 일 경우 주의
    # answer = ''.join(numbers)
    answer = str(int(''.join(numbers)))

    return answer