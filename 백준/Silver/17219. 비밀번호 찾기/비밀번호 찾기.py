N, M = map(int, input().split())
memo = {}
for i in range(N):
  s, p = input().split()
  memo[s] = p
for i in range(M):
  t = input()
  if t in memo:
    print(memo[t])
  else:
    None