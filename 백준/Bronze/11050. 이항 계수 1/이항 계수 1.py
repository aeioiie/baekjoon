# 이항 계수: nCk = n! / (n-k)!k!

N, K = map(int, input().split())

def fact(x):
    i = 1
    fact = 1
    while i <= x:
        fact *= i
        i += 1
    return fact

print(int(fact(N) / (fact((N-K)) * fact(K))))