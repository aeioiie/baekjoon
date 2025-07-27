n = int(input())

def fib_dp(x):
    dp = [0] * (x+1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[x]

print(fib_dp(n))