N1, D1 = map(int, input().split())
N2, D2 = map(int, input().split())

D3 = D1 * D2
N3 = N1*D2 + N2*D1

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

print(N3 // gcd(N3, D3), D3 // gcd(N3, D3))