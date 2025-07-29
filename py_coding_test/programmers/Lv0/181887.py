# 홀수 vs 짝수
def solution(num_list):
    answer = 0
    oddSum = 0
    evenSum = 0
    for idx, num in enumerate(num_list):
        if idx % 2 == 0:
            evenSum += num
        else:
            oddSum += num
    answer = max(oddSum, evenSum)
        
    return answer