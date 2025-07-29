# 배열 만들기 6
def solution(arr):
    answer = []
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1
        elif stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
    if len(stk) == 0:
        answer = [-1]
    else:
        answer = stk
    
    return answer