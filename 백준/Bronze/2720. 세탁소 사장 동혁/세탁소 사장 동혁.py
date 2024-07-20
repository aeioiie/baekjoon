T = int(input())
# Quarter: $0.25, Dime: $0.10, Nickel: $0.05, Penny: $0.01
Q = 25
D = 10
N = 5
P = 1
for i in range(T):
    C = int(input())
    q = C // Q
    d = C % Q // D
    n = C % Q % D // N
    p = C % Q % D % N // P

    print(f"{q} {d} {n} {p}")