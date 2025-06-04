M = int(input())
N = int(input())
prime_list = []

for i in range(M, N+1):
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i-1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(i)

if not prime_list:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))