import sys

def cantor(n: int) -> str:
    if n == 0:
        return "-"
    prev = cantor(n - 1)
    return prev + ' ' * len(prev) + prev

for line in sys.stdin:
    N = int(line.strip())
    print(cantor(N))