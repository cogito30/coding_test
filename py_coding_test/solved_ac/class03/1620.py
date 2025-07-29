# 나는야 포켓몬 마스터 이다솜
N, M = map(int, input().split())
poket_num = {}
num_poket = {}
for i in range(N):
    poketmon = input()
    poket_num[poketmon] = i+1
    num_poket[i+1] = poketmon

for _ in range(M):
    question = input()
    if question.isnumeric():
        print(num_poket[int(question)])
    else:
        print(poket_num[question])