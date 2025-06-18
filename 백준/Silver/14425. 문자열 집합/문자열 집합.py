N, M = map(int, input().split())
S = set()
count = 0

for i in range(N):
    s = input()
    S.add(s)

for i in range(M):
    s = input()
    if s in S:
        count += 1

print(count)