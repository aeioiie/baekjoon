'''
graph
  0 1 2 3 4
0
1     1 1 1
2   1     1
3   1     1
4   1 1 1

visited
0 1 2 3 4
0 1 1 1 1
'''
import queue

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = sorted({i for i in range(1, n+1) if graph[start][i] == 1} - visited)
        for v in nbr:
            dfs(graph, v, visited)

def bfs(graph, start):
    visited = {start}
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        v = que.get()
        print(v, end=' ')
        nbr = sorted({i for i in range(1, n+1) if graph[v][i] == 1} - visited)
        for u in nbr:
            visited.add(u)
            que.put(u)

dfs(graph, v, set())
print()
bfs(graph, v)