N = int(input())
list = []

for i in range(1, N):
    X = i
    sum = 0

    while X > 0:
        sum += X % 10
        X //= 10

    if sum + i == N:
        list.append(i)

if list:
    print(min(list))
else:
    print(0)