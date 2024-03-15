T = int(input())

for i in range(T):
  R, S = map(str, input().split())
  for i in S:
    P = i * int(R)
    print(P, end='')
  print()