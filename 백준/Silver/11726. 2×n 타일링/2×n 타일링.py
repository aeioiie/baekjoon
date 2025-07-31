import sys
input = sys.stdin.readline

n = int(input())

# n = 1 -> 1가지
# n = 2 -> 2가지
# n = 3 -> 3가지
# n = 4 -> 5가지

dp = [0] * 1001

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)