N, B = map(int, input().split())
con = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''

while N:
  ans += con[N%B]
  N //= B

print(ans[::-1])