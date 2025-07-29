# 최댓값
max_num = 0
max_idx = 0
for i in range(9):
    num = int(input())
    if max_num < num:
        max_idx = i
        max_num = num

print(max_num)
print(max_idx + 1)