import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [[False] * (M+1) for _ in range(N+1)]
dp[0][S] = True

for i in range(1, N+1):
    for j in range(M+1):
        if dp[i-1][j]:
            if j + V[i-1] <= M:
                dp[i][j + V[i-1]] = True
            if j - V[i-1] >= 0:
                dp[i][j - V[i-1]] = True

for vol in range(M, -1, -1):
    if dp[N][vol]:
        print(vol)
        break
else:
    print(-1)