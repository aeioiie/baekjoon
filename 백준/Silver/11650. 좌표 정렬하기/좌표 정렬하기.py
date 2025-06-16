N = int(input())
dot = []

for i in range(N):
    x, y = list(map(int, input().split()))
    dot.append((x, y))

dot.sort(key=lambda x: (x[0], x[1]))

for i in dot:
    print(i[0], i[1])