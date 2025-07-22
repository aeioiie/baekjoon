import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] *(N+1)
count = 0

for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True

def dfs(v):
    global visited
    visited[v] = True

    for i in range(1, N+1):
        if not visited[i] and graph[v][i]:
            dfs(i)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)