# 문자열 밀기
def solution(A, B):
    answer = -1
    N = len(A)
    A = A[::-1]
    B = B[::-1]
    queue = []
    for i in range(N):
        queue.append(A[i])

    for i in range(1, N+1):
        word = queue.pop(0)
        queue.append(word)
        print(i, queue, B)
        if B == ''.join(queue):
            answer = i
            break
        
    if answer == N:
        answer = 0
    return answer