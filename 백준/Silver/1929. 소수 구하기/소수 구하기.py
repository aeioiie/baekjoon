def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)