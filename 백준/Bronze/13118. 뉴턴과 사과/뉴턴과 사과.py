p1, p2, p3, p4 = map(int, input().split())
x, y, r = map(int, input().split())
p = [p1, p2, p3, p4]

ans = 0
for i in range(4):
    if p[i] == x:
        ans = i+1
        break

print(ans)