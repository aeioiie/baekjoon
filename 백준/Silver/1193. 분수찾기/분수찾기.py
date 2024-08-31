X = int(input())
l = 1

while X > l:
    X -= l
    l += 1

if l % 2 == 0:
    a = X
    b = l - X + 1
elif l % 2 == 1:
    a = l - X + 1
    b = X

print(f'{a}/{b}')