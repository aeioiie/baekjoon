N = int(input())
list = []

for i in range(N):
    x = int(input())
    list.append(x)

list.sort()

for i in list:
    print(i)