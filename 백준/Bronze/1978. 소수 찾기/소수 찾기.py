N = int(input())
A = list(map(int, input().split()))
c = 0

for i in A:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        c += 1

print(c)