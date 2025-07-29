# 패션왕 신해빈
T = int(input())

for _ in range(T):
    n = int(input())
    if n == 0:
        print(0)
        continue
    clothes = {}
    for _ in range(n):
        cloth, category = input().split()
        if clothes.get(category, None):
            clothes[category].append(cloth)
        else:
            clothes[category] = [cloth]
    
    answer = 1
    for category, cloth_list in clothes.items():
        answer *= (len(cloth_list) + 1)
    print(answer - 1)