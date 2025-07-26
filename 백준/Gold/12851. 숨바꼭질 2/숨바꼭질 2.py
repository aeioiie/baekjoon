from collections import deque

N, K = map(int, input().split())

max_location = 10 ** 5
visited = [-1] * (max_location + 1)
count = [0] * (max_location + 1)

# 5 - 10 - 9 - 18 - 17
# 5 - 4 - 8 - 16 - 17

def bfs():
    queue = deque()
    queue.append(N)
    visited[N] = 0
    count[N] = 1

    while queue:
        x = queue.popleft()

        for i in (x-1, x+1, 2*x):
            if 0 <= i <= max_location:
                if visited[i] == -1:
                    visited[i] = visited[x] + 1
                    count[i] = count[x]
                    queue.append(i)
                elif visited[i] == visited[x] + 1:
                    count[i] += count[x]

    print(visited[K])
    print(count[K])

bfs()