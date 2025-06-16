N = input()
num = []

for i in N:
    num.append(int(i))

num.sort(reverse=True)

for i in num:
    print(i, end='')