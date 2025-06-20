# 최대공약수(GCD)
# gcd(a, b) = gcd(b, a%b)
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a   
    
# 최소공배수(LCM)
# lcm(a, b) = a*b / gcd(a, b)
def lcm(a, b):
    return a*b // gcd(a, b)

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))