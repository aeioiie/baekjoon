a, b, c = map(int, input().split())
list = [a, b, c]

if max(list) < sum(list) - max(list):
    print(sum(list))
else:
    list.append(sum(list) - max(list) - 1)
    list.remove(max(list))
    print(sum(list))