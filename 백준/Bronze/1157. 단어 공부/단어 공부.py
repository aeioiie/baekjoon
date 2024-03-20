w = list(input().upper())
cnt = {}

for i in w:
    cnt[i] = cnt.get(i, 0) + 1

max_val = max(cnt.values())
max_keys = [key for key, val in cnt.items() if val == max_val]

if len(max_keys) > 1:
    print('?')
else:
    print(max_keys[0])