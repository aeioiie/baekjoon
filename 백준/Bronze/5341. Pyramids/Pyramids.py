def f(n):
    if n == 1:
        return 1
    else:
        return n + f(n-1)
    
while True:
    n = int(input())
    if n == 0:
        break
    print(f(n))