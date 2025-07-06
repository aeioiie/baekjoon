N = int(input())
real_divisor = list(map(int, input().split()))
real_divisor = sorted(real_divisor)

print(real_divisor[0] * real_divisor[-1])