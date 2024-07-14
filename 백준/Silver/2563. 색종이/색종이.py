n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for x_ in range(x, x+10):
        for y_ in range(y, y+10):
            if x_ >= 100 or y_ >= 100:
                break
            paper[x_][y_] = 1

sum = 0

for i in range(100):
    sum += paper[i].count(1)

print(sum)