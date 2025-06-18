n = int(input())
records = {}

for i in range(n):
    name, el = input().split()
    records[name] = el

# print(records)

incompany = []

for name, el in records.items():
    if el == 'enter':
        incompany.append(name)

incompany.sort(reverse=True)
for name in incompany:
    print(name)