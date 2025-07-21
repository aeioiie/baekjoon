N, M, V = map(int, input().split())

# dfs
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

'''
graph 0 1 2 3 4
0     - - - - -
1     - - 1 1 1
2     - 1 - - 1
3     - 1 - - 1
4     - 1 1 1 -
'''

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(v):
    global visited
    visited[v] = True
    print(v, end=' ')

    for i in range(1, N+1):
        if not visited[i] and graph[v][i]:
            dfs(i)

dfs(V)
print()

# bfs
visited = [False] * (N+1)
q = [V]
visited[V] = True

def bfs(v):
    global visited, q
    while q:
        v = q.pop(0)
        print(v, end=' ')

        for i in range(1, N+1):
            if not visited[i] and graph[v][i]:
                visited[i] = True
                q.append(i)


bfs(V)