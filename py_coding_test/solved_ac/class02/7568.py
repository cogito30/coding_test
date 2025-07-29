# 덩치
N = int(input())

people = []
for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

rank = [0 for _ in range(N)]
for i in range(N):
    idx = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            idx += 1
    rank[i] = idx

for i in rank:
    print(i)