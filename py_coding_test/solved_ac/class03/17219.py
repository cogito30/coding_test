# 비밀번호 찾기
N, M = map(int, input().split())
site = {}
for _ in range(N):
    name, password = input().split()
    site[name] = password

for _ in range(M):
    name = input()
    print(site[name])