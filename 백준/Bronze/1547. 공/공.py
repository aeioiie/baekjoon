M = int(input())
cup = [1, 2, 3]

for i in range(M):
    X, Y = map(int, input().split())
    a = cup.index(X)
    b = cup.index(Y)
    cup[a], cup[b] = cup[b], cup[a]

print(cup[0])