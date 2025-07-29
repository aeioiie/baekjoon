N = int(input())

# 10 -> 9 -> 3 -> 1
def cal(n):
    dp = [0] * (n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1 # -1
        if i % 2 == 0: # // 2
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0: # // 3
            dp[i] = min(dp[i], dp[i//3] + 1)
    
    return dp[n]

print(cal(N))