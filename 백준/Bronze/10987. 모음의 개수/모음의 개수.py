W = input()
cnt = 0

for i in W:
    if i in 'aeiou':
        cnt += 1

print(cnt)