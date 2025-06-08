a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

def f(n):
    return a1 * n + a0
def g(n):
    return n

for n in range(n0, 1000001):
    if f(n) > g(n) * c:
        print(0)
        break
else:
    print(1)