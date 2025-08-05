N = int(input())
nickname = set()
count = 0

for i in range(N):
    s = input()
    if s == "ENTER":
        current_count = len(nickname)
        nickname.clear()
        count += current_count
    else:
        nickname.add(s)

print(count + len(nickname))