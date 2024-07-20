N = int(input())

sum = 2

for i in range(1, N+1):
    sum += 2**(i-1)

print(sum**2)