K = int(input())
money = []

for i in range(K):
    n = int(input())

    if n == 0:
        money.pop()
    else:
        money.append(n)

print(sum(money))