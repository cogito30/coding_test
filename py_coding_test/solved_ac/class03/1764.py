# 듣보잡
N, M = map(int, input().split())
no_listen = set()
for _ in range(N):
    no_listen.add(input())
no_seen = set()
for _ in range(M):
    no_seen.add(input())

result = no_listen & no_seen
print(len(result))
result = list(result)
result.sort()
for name in result:
    print(name)


"""시간초과
N, M = map(int, input().split())
no_listen = []
for _ in range(N):
    no_listen.append(input())
no_seen = []
for _ in range(M):
    no_seen.append(input())

answer = []
for i in range(N):
    for j in range(M):
        if no_listen[i] == no_seen[j]:
            answer.append(no_listen[i])

answer.sort()
print(len(answer))
for name in answer:
    print(name)
"""