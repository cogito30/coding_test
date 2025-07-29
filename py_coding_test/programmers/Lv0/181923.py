# 수열과 구간 쿼리 2
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        sorted_arr = sorted(arr[s:e+1])
        for i in range(len(sorted_arr)):
            if sorted_arr[i] > k:
                answer.append(sorted_arr[i])
                break
            elif i == len(sorted_arr) - 1:
                answer.append(-1)
        
    return answer