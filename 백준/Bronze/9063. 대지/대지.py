N = int(input())
listX = []
listY = []

for i in range(N):
    x, y = map(int, input().split())
    listX.append(x)
    listY.append(y)

width = max(listX) - min(listX)
height = max(listY) - min(listY)

print(width * height)