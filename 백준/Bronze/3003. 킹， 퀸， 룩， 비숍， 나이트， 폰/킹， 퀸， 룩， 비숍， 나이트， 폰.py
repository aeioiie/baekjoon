# 킹 1 퀸 1 룩 2 비숍 2 나이트 2 폰 8

C = list(map(int, input().split()))

k = 1
q = 1
l = 2
b = 2
n = 2
p = 8

print(k - C[0], q - C[1], l - C[2], b - C[3], n - C[4], p - C[5])