from collections import deque

N = int(input())
num = list(map(int, input().split()))
dq = deque()

for i in range(N):
    dq.append((i+1, num[i]))

# 1 2 3 4 5
# 3 2 1 -3 -1
# 1 -3 -1 1 2
# 1 4 5 3 2

# print(dq)

result = []

while dq:
    ballon = dq.popleft() # dq[0]을 빼서 ballon에 저장
    number = ballon[0]
    move = ballon[1]
    result.append(number)

    if not dq:
        break

    if move > 0:
        for i in range(move-1):
            dq.append(dq.popleft())
    else:
        for i in range(-move):
            dq.appendleft(dq.pop())

print(*result)