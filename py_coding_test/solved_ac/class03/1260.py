# DFS와 BFS
## cur가 없는 경우 주의! graph.get(cur, []) 사용
N, M, V = map(int, input().split())
graph = {}
for _ in range(M):
    a, b = map(int, input().split())
    if graph.get(a, None):
        graph[a].append(b)
    else:
        graph[a] = [b]
    if graph.get(b, None):
        graph[b].append(a)
    else:
        graph[b] = [a]

for i in graph.values():
    i.sort()

visited1 = [False for _ in range(N + 1)]
visited2 = [False for _ in range(N + 1)]
def dfs(start, graph):
    result = []
    stack = []
    stack.append(start)
    while stack:
        cur = stack.pop()
        if not visited1[cur]:
            visited1[cur] = True
            result.append(cur)
            for next in graph.get(cur, [])[::-1]:
                stack.append(next)
    return result

def bfs(start, graph):
    result = []
    q = []
    q.append(start)
    visited2[start] = True
    result.append(start)
    while q:
        cur = q.pop(0)
        for next in graph.get(cur, []):
            if not visited2[next]:
                visited2[next] = True
                q.append(next)
                result.append(next)
    return result


result_dfs = dfs(V, graph)
print(' '.join(map(str, result_dfs)))

result_bfs = bfs(V, graph)
print(' '.join(map(str, result_bfs)))


"""
N, M, V = map(int, input().split())
graph = {}

# 인접 리스트 구성
for _ in range(M):
    a, b = map(int, input().split())
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)

# 연결 노드 오름차순 정렬
for i in range(1, N+1):
    if i not in graph:
        graph[i] = []
    else:
        graph[i].sort()

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

def dfs(start):
    result = []
    stack = [start]
    while stack:
        cur = stack.pop()
        if not visited1[cur]:
            visited1[cur] = True
            result.append(cur)
            for next in reversed(graph.get(cur, [])):  # 작은 숫자부터 방문
                stack.append(next)
    return result

def bfs(start):
    result = []
    q = [start]
    visited2[start] = True
    while q:
        cur = q.pop(0)
        result.append(cur)
        for next in graph.get(cur, []):
            if not visited2[next]:
                visited2[next] = True
                q.append(next)
    return result

result_dfs = dfs(V)
result_bfs = bfs(V)

print(' '.join(map(str, result_dfs)))
print(' '.join(map(str, result_bfs)))


"""