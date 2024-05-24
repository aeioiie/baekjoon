def GetSome(a, b):
  if b == 1:
    return a
  halfpower = GetSome(a, b//2)
  if b & 1: # 홀수일 때
    return halfpower * halfpower * a % c
  else:
    return halfpower * halfpower % c

a, b, c = map(int, input().split())
print(GetSome(a, b) % c)