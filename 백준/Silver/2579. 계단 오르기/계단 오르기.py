S = int(input())
score = [int(input()) for _ in range(S)]

dp = [0] * S

if S == 1: # 계단이 하나라면 계단 하나의 점수 그 자체
    print(score[0])
elif S == 2: # 계단이 두 개라면 계단 두 개의 점수의 합
    print(score[0] + score[1])
else: # 연속된 세 개의 계단을 모두 밟을 수 없으므로 조건 나눔
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])

    for i in range(3, S):
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])
        
    print(dp[-1])