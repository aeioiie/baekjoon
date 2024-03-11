N, M = map(int, input().split())
basket = []

for _ in range(N):
  basket.append(_+1)

for _ in range(M):
  i, j = map(int, input().split())
  basket_reversed = basket[i-1: j]
  basket_reversed = basket_reversed[::-1]
  basket[i-1:j] = basket_reversed 

for _ in basket:
  print(_, end=' ')