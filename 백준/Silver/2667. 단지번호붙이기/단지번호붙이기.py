N = int(input())
square_map = [list(map(int, list(input()))) for _ in range(N)]

# 방향 벡터
# 상: (0, -1), 하: (0, 1), 좌: (-1, 0), 우: (1, 0)
dx = [0, 0, -1, 1] # 좌, 우
dy = [-1, 1, 0, 0] # 상, 하

visited = [[False] * N for _ in range(N)]
house_count = []

def dfs(x, y):
    global visited
    visited[y][x] = True
    count = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
    
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[ny][nx] and square_map[ny][nx]:
                count += dfs(nx, ny)
    
    return count

for y in range(N):
    for x in range(N):
        if square_map[y][x] == 1 and not visited[y][x]:
            house_count.append(dfs(x, y))

house_count.sort()

print(len(house_count))
for count in house_count:
    print(count)