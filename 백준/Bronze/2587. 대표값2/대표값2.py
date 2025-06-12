list = []

for i in range(5):
    n = int(input())
    list.append(n)
    list.sort()

print(int(sum(list) / len(list)))
print(list[2])