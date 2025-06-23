T = int(input())

nums = []
max_n = 0

for i in range(T):
    N = int(input())
    nums.append(N)
    if N > max_n:
        max_n = N

isPrime = [True] * (max_n+1)
isPrime[0] = isPrime[1] = False

for i in range(2, int(max_n**0.5) + 1):
    if isPrime[i]:
        for j in range(i*i, max_n+1, i):
            isPrime[j] = False
    
for N in nums:
    count = 0
    for i in range(2, (N//2) + 1):
        if isPrime[i] and isPrime[N-i]:
            count += 1

    print(count)