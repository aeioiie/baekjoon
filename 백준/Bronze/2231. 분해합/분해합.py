N = int(input())
list = []

# N = 256 = 245 + 2 + 4 + 5
# M = 245

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