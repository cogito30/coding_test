# 소인수분해
def solution(n):
    answer = []
    num_list = set()
    for i in range(2, n+1):
        while n >= i:
            if n % i == 0:
                n //= i
                num_list.add(i)
            else:
                break
    # set은 순서를 보장하지 않음
    answer = sorted(list(num_list))
    return answer