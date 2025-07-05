# 조합: mCn = m! / (m-n)! * n!

T = int(input())

def fact(x):
    i = 1
    fact = 1
    while i <= x:
        fact *= i
        i += 1
    return fact

for i in range(T):
    N, M = map(int, input().split())
    print(int(fact(M) / (fact((M-N)) * fact(N))))