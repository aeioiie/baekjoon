import sys
input = sys.stdin.readline

N = int(input())
time = []
profit = []

for i in range(N):
    T, P = map(int, input().split())
    time.append(T)
    profit.append(P)

dp = [0] * (N+1) # dp[i] = i일까지 얻을 수 있는 최대 이익

for i in range(N):
    dp[i+1] = max(dp[i+1], dp[i]) # 상담을 하지 않는 경우

    if i + time[i] <= N:  # 상담을 할 수 있는 경우
        dp[i + time[i]] = max(dp[i + time[i]], dp[i] + profit[i])

print(dp[N])

'''
N = int(input())
time = [0] * (N+1)
profit = [0] * (N+1)
dp = [0] * (N+2)

for i in range(1, N+1):
    t, p = map(int, input().split())
    time[i] = t
    profit[i] = p

for i in range(N, 0, -1):
    if i + time[i] - 1 <= N:
        dp[i] = max(dp[i+1], profit[i] + dp[i + time[i]])
    else:
        dp[i] = dp[i+1]

print(dp[1])
'''

