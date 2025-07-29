# 연결 요소의 개수
with open('./solved_ac/class03/test.txt', 'r') as f:
    N, M = map(int, f.readline().split())
    graph = {}
    for _ in range(M):
        u, v = map(int, f.readline().split())
        if graph.get(u, None) and graph.get(v, None):
            graph[u].append(v)
            graph[v].append(u)
        else:
            graph[u] = [v]
            graph[v] = [u]
print(graph)
        
"""
N, M = map(int, input().split())
graph = {}
for _ in range(M):
    u, v = map(int, input().split())
"""

def bfs(start, graph):
    
