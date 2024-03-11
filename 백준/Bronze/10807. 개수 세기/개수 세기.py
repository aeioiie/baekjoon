N = int(input())
A = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(N):
  if A[i] == v:
    cnt += 1
    
print(cnt)