# 소수 만들기
def check_prime(num):
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    len_num = len(nums)
    for i in range(len_num):
        for j in range(i+1, len_num):
            for k in range(j+1, len_num):
                if check_prime(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer