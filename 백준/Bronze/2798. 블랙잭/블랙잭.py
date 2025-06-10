N, M = map(int, input().split())
c = list(map(int, input().split()))

s = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = c[i] + c[j] + c[k]
            if sum <= M:
                s = max(s, sum)

print(s)