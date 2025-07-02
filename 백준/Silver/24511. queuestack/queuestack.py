from collections import deque

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = int(input())
C = list(map(int, input().split()))
# 만약 A 원소가 0이면 큐, 1이면 스택
# 큐: FIFO, 스택: LIFO

qs = deque([])

for i in range(N):
    if A[i] == 0:
        qs.append(B[i])

for i in range(M):
    qs.appendleft(C[i])
    print(qs.pop(), end=' ')