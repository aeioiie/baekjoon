n, b = input().split()

a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0

for i in range(len(n)):
    ans += a.index(n[i]) * int(b)** (len(n) - 1 - i)

print(ans)