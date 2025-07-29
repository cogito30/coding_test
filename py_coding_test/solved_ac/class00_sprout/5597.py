# 과제 안 내신 분..?
check_list = [0 for _ in range(30)]
for i in range(28):
    num = int(input())
    check_list[num-1] = 1

for i in range(30):
    if check_list[i] == 0:
        print(i+1)
    