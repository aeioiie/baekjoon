from collections import deque

N, K = map(int, input().split())

# 5 17
# 5 - 10 - 9 - 18 - 17 -> 4초

max_location = 10 ** 5
visited = [0] * (max_location + 1)

def bfs():
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            break

        for i in (x-1, x+1, 2*x):
            if 0 <= i <= max_location and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)

bfs()