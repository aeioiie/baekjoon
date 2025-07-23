import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

# 방향 벡터
# 상: (0, -1), 하: (0, 1), 좌: (-1, 0), 우: (1, 0)
dx = [0, 0, -1, 1] # 좌, 우
dy = [-1, 1, 0, 0] # 상, 하

def dfs(x, y):
    global visited
    visited[y][x] = True

    for d in range(4): # 상하좌우 탐색
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < M and 0 <= ny < N:
            if not visited[ny][nx] and graph[ny][nx]: # 방문되지 않고, 배추가 있는 경우 dfs 함수 호출
                dfs(nx, ny)

for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for j in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    worm_count = 0

    for y in range(N):
        for x in range(M):
            if graph[y][x] and not visited[y][x]:
                dfs(x, y)
                worm_count += 1
    
    print(worm_count)