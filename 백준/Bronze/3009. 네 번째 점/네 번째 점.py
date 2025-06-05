x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

listX = [x1, x2, x3]
listY = [y1, y2, y3]

for i in range(3):
    if listX.count(listX[i]) == 1:
        x = listX[i]
    if listY.count(listY[i]) == 1:
        y = listY[i]

print(x, y)