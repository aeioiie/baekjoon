N, M = map(int, input().split())
basket = []
for _ in range(N):
  basket.append(0)

for _ in range(M):
  i, j, k = map(int, input().split())
  if (j-i) != 0:
    for _ in range(j-i+1):
      basket[i-1] = k
      i += 1
  else:
    basket[i-1] = k

for _ in basket:
  print(_, end=' ')