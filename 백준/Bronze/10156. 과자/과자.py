K, N, M = map(int, input().split())
parent = (K * N) - M

if parent < 0:
    print(0)
else:
    print(parent)