# 나무 자르기
"""
with open('./solved_ac/class03/test.txt', 'r') as f:
    N, M = map(int, f.readline().split())
    trees = list(map(int, f.readline().split()))
"""

N, M = map(int, input().split())
trees = list(map(int, input().split()))


start = 0
end = max(trees)
while start <= end:
    total_length = 0
    mid = (start + end) // 2
    
    # 나무를 자를 수 있는 조건(자를 길이보다 클 때)
    for i in trees:
        if i >= mid:
            total_length += i - mid

    if total_length >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)