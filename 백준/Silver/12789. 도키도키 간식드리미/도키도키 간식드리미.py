def temporary(num):
    temp = []
    target = 1

    for i in num:
        while temp and temp[-1] == target:
            temp.pop()
            target += 1
        if i == target:
            target += 1
        else:
            temp.append(i)

    while temp and temp[-1] == target:
        temp.pop()
        target += 1

    if not temp:
        return "Nice"
    else:
        return "Sad"

N = int(input())
num = list(map(int, input().split()))

print(temporary(num))