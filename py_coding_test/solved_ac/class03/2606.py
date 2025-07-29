# 바이러스
## cur가 없는 경우를 대비하여 virus.get() 사용
N = int(input())
T = int(input())
virus = {}
for _ in range(T):
    a, b = map(int, input().split())
    if virus.get(a, None):
        virus[a].append(b)
    else:
        virus[a] = [b]
    if virus.get(b, None):
        virus[b].append(a)
    else:
        virus[b] = [a]
    
visited = [False for _ in range(N+1)]
visited[0] = True

def bfs(start, virus):
    count = 0
    q = []
    q.append(start)
    visited[start] = True
    while q:
        cur = q.pop(0)
        for next in virus.get(cur,[]):
            if not visited[next]:
                visited[next] = True
                q.append(next)
                count += 1
    return count


answer = bfs(1, virus)
print(answer)