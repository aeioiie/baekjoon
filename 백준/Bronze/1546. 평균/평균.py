N = int(input())
S = list(map(int, input().split()))
M = max(S)
score_rigged = []

for i in range(len(S)):
  score_rigged.append(S[i] / M * 100)
  
print(sum(score_rigged) / len(score_rigged))