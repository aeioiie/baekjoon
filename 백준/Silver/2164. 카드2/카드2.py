from collections import deque

def card(c):
    while len(c) > 1:
        c.popleft()
        c.append(c.popleft())

    return c[0]

N = int(input())
c = deque(range(1, N+1))

print(card(c))