# 입국심사
def solution(n, times):
    answer = 0
    maxTime = n*max(times)
    minTime = n//len(times) * min(times)
    
    while minTime <= maxTime:
        totalNum = 0
        currentTime = (maxTime + minTime) // 2
        for time in times:
            totalNum += currentTime // time
            # if totalNum >= n:
            #     break
        # 실패 코드        
        # if totalNum > n:
        #     maxTime = currentTime - 1
        # elif totalNum == n:
        #     answer = currentTime
        #     break
        if totalNum >= n:
            maxTime = currentTime - 1
            answer = currentTime
        elif totalNum < n:
            minTime = currentTime + 1
        
    return answer