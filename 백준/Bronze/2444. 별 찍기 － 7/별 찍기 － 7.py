N = int(input())

for i in range(1, N+1):
  print(' ' * (N-i) + '*' * (i*2-1))
for i in range(1, N):
  print(' ' * i + '*' * ((N-i)*2-1))