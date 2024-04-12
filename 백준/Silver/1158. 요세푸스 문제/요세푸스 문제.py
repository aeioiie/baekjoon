from collections import deque

N, K = map(int, input().split())
queue = deque(list(range(1, N+1)))
print('<', end='')

while len(queue) > 1:
  for i in range(K-1):
    queue.append(queue.popleft())

  print(queue.popleft(), end=', ')

print(queue.popleft(), end='')
print('>')