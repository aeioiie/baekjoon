while True:
    n = int(input())
    count = 0

    if n == 0:
        break

    isPrime = [True] * (2*n + 1)
    isPrime[0] = isPrime[1] = False

    for i in range(2, int((2*n)**0.5) + 1):
        if isPrime[i]:
            for j in range(i*i, 2*n + 1, i):
                isPrime[j] = False

    for i in range(n+1, 2*n + 1):
        if isPrime[i]:
            count += 1
    print(count)